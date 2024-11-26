from django.shortcuts import render
from .models import Tools
import os

# Create your views here.
def tools_list(request):
    """数据列表"""
    # 去数据库中获取所有数据
    tools = Tools.objects.all().order_by("-tools_freq")
    return render(request, 'tools/list_tools.html', {'tools': tools})
def tools_use(request, tools_name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_ip = request.META['REMOTE_ADDR']
    if request.method == "GET":
        return render(request, 'tools/tools_{}_use.html'.format(tools_name), {'tools_name': tools_name})
    # elif request.method == "POST":
    #     # result_path = get_result_path(BASE_DIR, tools_name)
    #     result_path = "./"
    #     # 从下面定义的函数中返回script_files和input_files.
    #     script_files, input_files = globals()[tools_name](request)
    #     print("input_files: ", input_files)
    #     python_script = f"python3 {BASE_DIR}/rootpath_tools/project_{tools_name}/{tools_name}.py {script_files}"
    #     print("python_script: ", python_script)
        
    #     # 更新tools的使用频率
    #     tools = Tools.objects.get(tools_name=tools_name)
    #     tools.tools_freq += 1
    #     tools.save()

    #     # 这一类工具是需要特殊处理的，因为这一类工具需要将用户上传的文件保存到服务器上，然后再调用python脚本进行处理

    #     # 这一类工具是不需要特殊处理的，直接调用python脚本进行处理
    #     return save_file(request, result_path, python_script, input_files)
 