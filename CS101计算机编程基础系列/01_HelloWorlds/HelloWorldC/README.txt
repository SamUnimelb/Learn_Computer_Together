1. Visual Studio Code C/C++ 使用教程：https://code.visualstudio.com/docs/cpp/config-mingw；
2. Mingw编译器建议从：https://sourceforge.net/projects/mingw/ 进行下载
3. 若Debug启动失败，需要检查项目中的launch.json文档中.exe文件的路径；
4. 若还是不正常，需要检查系统编码是否为UTF-8，见：https://stackoverflow.com/questions/69619818/vscode-unable-to-start-debugging-unexpected-gdb-output-from-the-command-envi/70312326#70312326
改变系统编码方式在“控制面板-时钟和区域-更改系统区域方式-Beta版：使用Unicode UTF-8 提供全球语言支持”