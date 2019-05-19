# Agile
*一个在线风险评估系统*

目前支持相乘法，矩阵法为核心的整个评估流程，用户登录注册，生成word报表和资产风险柱状图，历史评估系统修改删除等功能；后端有完善的多进程日志系统。

# 开发过程简述
人员分工：后端1人，前端1人，全栈1人(全栈主要写前端)

敏捷开发第一轮迭代：完成了用户登录注册，以矩阵法相乘法为核心的整个评估流程，并且进行了前后端分别的单元测试和前后端对接后的整体测试

敏捷开发第一轮迭代获得的可部署向用户展示的成品：[v0.6](https://github.com/voldemortX/Agile/tree/v0.6/backend)

敏捷开发第二轮迭代：增加了word报表和资产风险柱状图生成功能，历史评估系统修改删除功能，并且进行了前后端分别的单元测试和前后端对接后的整体测试

敏捷开发第二轮迭代获得的可部署向用户展示的成品：[v1.0](https://github.com/voldemortX/Agile/tree/v1.0/backend)

敏捷开发“第三轮迭代”：进行了一些程序bug修复，界面可用性改善，单元测试覆盖率的提升和文档的整理。

敏捷开发最终版本的部署版本所需更改直接在 [v1.0](https://github.com/voldemortX/Agile/tree/v1.0/backend) 做出；单元测试覆盖率的提升等非部署性改动体现在最终的master分支，dev分支由于要保留其url有其他用处所以暂未删除。

# 架构与整体开发环境
整体架构： **前后端分离**

API集成化测试平台（包含MOCK请求）：[YApi](https://github.com/YMFE/yapi "YApi")


前端架构：类似于MVC

前端开发环境：[Vue](https://cn.vuejs.org/ "Vue") + ([Element](https://github.com/ElemeFE/element "Element") + [Echarts](https://echarts.baidu.com/index.html "Echarts") + [docx](https://github.com/dolanmiu/docx "docx"))

前端单元测试环境：[Vue-test-utils](https://github.com/vuejs/vue-test-utils "Vue-test-utils") + [Mocha + Chai](https://github.com/vuejs/vue-cli/blob/dev/packages/%40vue/cli-plugin-unit-mocha/README.md "Mocha + Chai")


后端架构：类似于MVC

后端开发环境：[Flask](http://flask.pocoo.org/docs/1.0/ "Flask") + MySql

后端单元测试环境：[Pytest](https://docs.pytest.org/en/latest/ "Pytest") + [Pytest-cov](https://github.com/pytest-dev/pytest-cov "Pytest-cov")

# 部署与开发使用方式
部署版本：[v1.0](https://github.com/voldemortX/Agile/tree/v1.0/backend)

部署方式：首先 [建立数据库](https://github.com/voldemortX/Agile/blob/v1.0/dbCreate.sql) ，并在params.py修改数据库URI，最后启动服务器方法根据实际情况（e.g. python server.py）, [具体环境细节](https://github.com/voldemortX/Agile/tree/v1.0/backend/configs.txt)

前端开发测试等直接使用 [Vue-cli 3](https://cli.vuejs.org/zh/) 提供的集成开发测试可视化UI, *IDE玩家推荐使用 WebStorm*

后端开发测试等按照 [说明](https://github.com/voldemortX/Agile/tree/v1.0/backend/configs.txt) 进行，*IDE玩家推荐使用 Pycharm*

# 在该环境开发容易遇到的几个大坑
1. Vue-cli里面直接build得到的html和js,css等放在一起，部署时需要对应把html放到templates文件夹，其他放到static文件夹并 **对应将index.html里的引用路径加上/static**

2. 前端与他人协作需要先 [这样操作](https://github.com/voldemortX/Agile/blob/v1.0/frontend/README.md)

3. Vue-test-utils对第三方UI库的支持尚不完善，具体情况可以参考这个 [issue](https://github.com/vuejs/vue-test-utils/issues/1221)

4. Pytorch常与Pytest-cov不兼容，具体情况可以参考这个 [issue](https://github.com/pytest-dev/pytest-cov/issues/293) ，建议使用Conda创建新虚拟环境开发

5. Flask-SqlAlchemy这个库的实现存在缓存不一致问题，建议所有数据库操作采用SqlAlchemy的原始方法（假设有个表映射的类叫User）：e.g. 不要使用 ```User.query.all()``` , 改为使用 ```current_app.db.session.query(User).all()```

