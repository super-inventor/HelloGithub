#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
启动脚本
运行方式: python run.py
"""

from app import app

if __name__ == '__main__':
    print("启动 Flask 炫彩项目...")
    print("访问 http://127.0.0.1:5000 查看效果")
    print("按 Ctrl+C 停止服务")
    app.run(debug=True, host='0.0.0.0', port=5000)
