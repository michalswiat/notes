# Installing Nvidia CUDA lib

Follow:
https://developer.nvidia.com/cuda-12-2-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network

Installed in directory:
usr/local/cuda-12/

Export it to PATH variable:
export PATH="/usr/local/cuda-12/bin:$PATH"

# Installing llama_cpp for python:
CUDACXX=/usr/local/cuda-12/bin/nvcc CMAKE_ARGS="-DLLAMA_CUBLAS=on
-DCMAKE_CUDA_ARCHITECTURES=all-major" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade

[source] https://stackoverflow.com/questions/76963311/llama-cpp-python-not-using-nvidia-gpu-cuda

# Installing tensorflow
pip install "tensorflow[and-cuda]"

Check if GPU can be found:
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
