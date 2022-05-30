# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.main:app",
                host="0.0.0.0",
                port=5005,
                reload=True
                )