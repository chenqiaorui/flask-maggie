# Asynchronous Tasks with Flask and Celery

Example of how to handle background processes with Flask, Celery, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/flask-and-celery/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to [http://localhost:5004](http://localhost:5004) to view the app or to [http://localhost:5556](http://localhost:5556) to view the Flower dashboard.

Trigger a new task:

```sh
$ curl http://localhost:5004/api/tasks -H "Content-Type: application/json" 
       -H "X-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2ODI0NzkxMzh9.v678otVqcDZG-I6I38ijH5_RpC3X_wgfIWWvxih2naw"
       --data '{"type": 0}'
```

Check the status:

```sh
$ curl http://localhost:5004/api/tasks/<TASK_ID>/ -H "X-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2ODI0NzkxMzh9.v678otVqcDZG-I6I38ijH5_RpC3X_wgfIWWvxih2naw"
```

### About Celery books
[https://www.celerycn.io/](https://www.celerycn.io/)

### 功能
这个项目可以做什么?
```
- 提供web服务
- jwt鉴权
- 添加队列任务
- 用户登录和注册、获取用户信息

技术栈：
- celery队列
- flask web框架
```