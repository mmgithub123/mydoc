
jvm 调优：

执行的过程中为了保证dump的信息是可靠的，所以会暂停应用， 线上系统慎用。
想要浏览heap dump，你可以使用jhat(Java堆分析工具)读取生成的文件。
文件dump下来以后，可以使用Eclipse的MAT插件进行查看
如果日常开发用的是eclipse的话，可以直接安装这个插件，如果不是的话，这个插件也可以独立运行
