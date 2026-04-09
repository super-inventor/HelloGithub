from setuptools import setup, find_packages

setup(
    name="flask-rainbow-project",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=3.0.0",
    ],
    author="CYL",
    description="一个使用 Flask 框架生成的炫彩效果网页项目，支持白天/黑夜主题切换",
    python_requires=">=3.8",
)
