var app = angular.module('app', ['ngRoute']);

app.controller('PostCtrl', ['$routeParams', '$http',
        function($routeParams, $http) {
            var app = this;
            app.postId = $routeParams.postId
            $http.get('/api/post/' + app.postId).success(function(data) {
                app.post = data;
            });
            app.addComment = function() {
                var content = document.getElementById('newContent').value;
                $http.post('/api/comment', {'content': content, 'post_id': app.postId})
                    .success(function (data) {
                        app.post.comments.push(data);;;;
                        document.getElementById('newContent').value = '';
                    })
            };
            app.updateComment = function(comment, up) {
                if (up) {
                    comment.score++;
                } else {
                    comment.score--;
                }
                $http.put('/api/comment/' + comment.id, comment);
            }
        }]);

app.controller('AppCtrl', function($http) {
    var app = this;
    $http.get('/api/post').success(function (data) {
        app.posts = data.objects;
    });

    app.addPost = function() {
	var title = document.getElementById('newTitle').value,
	    link =  document.getElementById('newLink').value;
        $http.post('/api/post', {'title': title, 'link': link})
            .success(function (data) {
                app.posts.push(data);
                document.getElementById('newTitle').value = '';
                document.getElementById('newLink').value = '';
            });
    };

    app.deletePost = function(post) {
       $http.delete('/api/post/' + post.id).success(function (response) {
           app.posts.splice(app.posts.indexOf(post), 1);
       });
    };

    app.updatePost = function(post, up) {
        if (up) {
            post.score++;
        } else {
            post.score--;
        }
       $http.put('/api/post/' + post.id, post);
    };
});

app.config(['$routeProvider',
        function($routeProvider) {
            $routeProvider.
                when('/posts', {
                    templateUrl: 'partials/post-list.html',
                    controller: 'AppCtrl'
                }).
                when('/posts/:postId', {
                    templateUrl: 'partials/post-detail.html',
                    controller: 'PostCtrl'
                }).
                otherwise({
                    redirectTo: '/posts'
                });
        }]);

