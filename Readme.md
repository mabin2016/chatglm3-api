### chatglm3-6b模型本地调用


##### 模型下载
```
git lfs install
git clone https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git
```

###### 启动接口
```
# 创建虚拟环境
conda create -n test python=3.11 -y

# 安装依赖
conda activate test && cd app && pip install -r requirements.txt

# 设置模型路径
export MODEL_PATH=your_model_path

 # 启动API接口
uvicorn api:app --reload
```

###### 测试接口
```
# 新开一个终端
conda activate test && cd app

export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export OPENAI_API_KEY=EMPTY
export TAVILY_API_KEY=your_tavily_api_key

python agent.py
```

###### 运行效果
- (运行截图)[]
- (程序流程)[]

##### GPU配置
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.82.01    Driver Version: 470.82.01    CUDA Version: 11.8     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA A10          Off  | 00000000:00:08.0 Off |                    0 |
|  0%   41C    P8    16W / 150W |      0MiB / 22731MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

##### FQA
- Q: 启动API接口报错
```
 File "/home/pai/envs/a/lib/python3.10/site-packages/torch/cuda/__init__.py", line 302, in _lazy_init
    torch._C._cuda_init()
RuntimeError: The NVIDIA driver on your system is too old (found version 11080). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx  Alternatively, go to: https://pytorch.org  to install a PyTorch version that has been compiled with your version of the CUDA driver.
```
A: 强制重装pytorch
```
pip install torch==2.1.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```