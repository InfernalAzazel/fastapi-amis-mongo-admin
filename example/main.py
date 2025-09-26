from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi_amis_admin.amis.components import App, PageSchema, Page


app = FastAPI()


def get_app_config():
    """获取应用配置"""
    amis_app = App()
    amis_app.type = 'app'
    amis_app.brandName = "FastAPI Amis 多页面示例"
    amis_app.logo = "https://suda.cdn.bcebos.com/images%2F2021-01%2Fdiamond.svg"
    
    # 使用 APageSchema 类来配置页面
    # 创建首页
    home_page = PageSchema(
        label="首页",
        icon="fa fa-home",
        url="/",
        isDefaultPage=True,
        schema={
            "type": "page",
            "title": "欢迎页面",
            "body": {
                "type": "container",
                "body": [
                    {
                        "type": "tpl",
                        "tpl": "<h1>欢迎使用 FastAPI Amis 多页面应用</h1><p>这是一个使用 APageSchema 的示例应用</p>"
                    },
                    {
                        "type": "grid",
                        "columns": [
                            {
                                "type": "card",
                                "header": {
                                    "title": "表单页面",
                                    "subTitle": "用户信息表单"
                                },
                                "body": {
                                    "type": "button",
                                    "label": "访问表单页面",
                                    "level": "primary",
                                    "actionType": "url",
                                    "url": "/form"
                                }
                            },
                            {
                                "type": "card", 
                                "header": {
                                    "title": "表格页面",
                                    "subTitle": "数据展示表格"
                                },
                                "body": {
                                    "type": "button",
                                    "label": "访问表格页面",
                                    "level": "success",
                                    "actionType": "url",
                                    "url": "/table"
                                }
                            },
                            {
                                "type": "card",
                                "header": {
                                    "title": "卡片页面", 
                                    "subTitle": "信息卡片展示"
                                },
                                "body": {
                                    "type": "button",
                                    "label": "访问卡片页面",
                                    "level": "info",
                                    "actionType": "url",
                                    "url": "/cards"
                                }
                            }
                        ]
                    }
                ]
            }
        }
    )
    
    # 创建表单页面
    form_page = PageSchema(
        label="表单页面",
        icon="fa fa-edit",
        url="/form",
        schema={
            "type": "page",
            "title": "用户信息表单",
            "body": {
                "type": "form",
                "mode": "horizontal",
                "api": "/api/saveForm",
                "body": [
                    {
                        "label": "姓名",
                        "type": "input-text",
                        "name": "name",
                        "required": True,
                        "placeholder": "请输入您的姓名"
                    },
                    {
                        "label": "邮箱",
                        "type": "input-email",
                        "name": "email",
                        "required": True,
                        "placeholder": "请输入您的邮箱"
                    },
                    {
                        "label": "年龄",
                        "type": "input-number",
                        "name": "age",
                        "min": 1,
                        "max": 120
                    },
                    {
                        "label": "性别",
                        "type": "select",
                        "name": "gender",
                        "options": [
                            {"label": "男", "value": "male"},
                            {"label": "女", "value": "female"}
                        ]
                    },
                    {
                        "label": "爱好",
                        "type": "checkboxes",
                        "name": "hobbies",
                        "options": [
                            {"label": "读书", "value": "reading"},
                            {"label": "运动", "value": "sports"},
                            {"label": "音乐", "value": "music"},
                            {"label": "旅行", "value": "travel"}
                        ]
                    },
                    {
                        "type": "submit",
                        "label": "提交",
                        "level": "primary"
                    }
                ]
            }
        }
    )
    
    # 创建表格页面
    table_page = PageSchema(
        label="表格页面",
        icon="fa fa-table",
        url="/table",
        schema={
            "type": "page",
            "title": "用户数据表格",
            "body": {
                "type": "table",
                "api": "/api/users",
                "columns": [
                    {
                        "name": "id",
                        "label": "ID",
                        "type": "text"
                    },
                    {
                        "name": "name",
                        "label": "姓名",
                        "type": "text"
                    },
                    {
                        "name": "email",
                        "label": "邮箱",
                        "type": "text"
                    },
                    {
                        "name": "age",
                        "label": "年龄",
                        "type": "text"
                    },
                    {
                        "name": "gender",
                        "label": "性别",
                        "type": "mapping",
                        "map": {
                            "male": "<span class='label label-info'>男</span>",
                            "female": "<span class='label label-warning'>女</span>"
                        }
                    },
                    {
                        "type": "operation",
                        "label": "操作",
                        "buttons": [
                            {
                                "type": "button",
                                "label": "编辑",
                                "level": "link"
                            },
                            {
                                "type": "button",
                                "label": "删除",
                                "level": "link",
                                "className": "text-danger"
                            }
                        ]
                    }
                ]
            }
        }
    )
    

    print(home_page.as_page_body())
    # 设置页面列表
    amis_app.pages = [
        # home_page.model_dump(exclude_none=True),
       {
          "children": [
            {
              "label": "子页面",
              "url": "/",
              "schema": {
                "type": "page",
                "title": "Page A"
              }
            }
          ]
        },

        PageSchema(
            children=[
                PageSchema(
                    label="卡片页面",
                    icon="fa fa-th-large",
                    url="/cards",
                    schema={
                        "type": "page",
                        "title": "信息卡片展示",
                        "body": {
                            "type": "grid",
                            "columns": [
                                {
                                    "type": "card",
                                    "header": {
                                        "title": "系统信息",
                                        "subTitle": "当前系统状态"
                                    },
                                    "body": {
                                        "type": "property",
                                        "items": [
                                            {"label": "系统版本", "content": "FastAPI Amis v1.0"},
                                            {"label": "运行时间", "content": "2天3小时"},
                                            {"label": "内存使用", "content": "45%"},
                                            {"label": "CPU使用", "content": "12%"}
                                        ]
                                    }
                                },
                                {
                                    "type": "card",
                                    "header": {
                                        "title": "用户统计",
                                        "subTitle": "用户数据概览"
                                    },
                                    "body": {
                                        "type": "property",
                                        "items": [
                                            {"label": "总用户数", "content": "1,234"},
                                            {"label": "活跃用户", "content": "856"},
                                            {"label": "新增用户", "content": "23"},
                                            {"label": "在线用户", "content": "67"}
                                        ]
                                    }
                                },
                                {
                                    "type": "card",
                                    "header": {
                                        "title": "快速操作",
                                        "subTitle": "常用功能入口"
                                    },
                                    "body": {
                                        "type": "grid",
                                        "columns": [
                                            {
                                                "body": {
                                                    "type": "button",
                                                    "label": "添加用户",
                                                    "level": "primary",
                                                    "size": "sm"
                                                }
                                            },
                                            {
                                                "body": {
                                                    "type": "button",
                                                    "label": "导出数据",
                                                    "level": "success",
                                                    "size": "sm"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                )
            ]
        ),
    ]
    
    return amis_app


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """首页"""
    amis_app = get_app_config()
    return HTMLResponse(content=amis_app.render())


@app.get("/form", response_class=HTMLResponse)
async def form_page():
    """表单页面"""
    amis_app = get_app_config()
    return HTMLResponse(content=amis_app.render())


@app.get("/table", response_class=HTMLResponse)
async def table_page():
    """表格页面"""
    amis_app = get_app_config()
    return HTMLResponse(content=amis_app.render())


@app.get("/cards", response_class=HTMLResponse)
async def cards_page():
    """卡片页面"""
    amis_app = get_app_config()
    return HTMLResponse(content=amis_app.render())


# 添加一个通配符路由来处理所有其他路径
@app.get("/{path:path}", response_class=HTMLResponse)
async def catch_all(path: str):
    """捕获所有其他路径，返回应用配置"""
    amis_app = get_app_config()
    return HTMLResponse(content=amis_app.render())


# API 接口
@app.post("/api/saveForm")
async def save_form(request: Request):
    """保存表单数据"""
    form_data = await request.json()
    # 这里可以保存到数据库
    return JSONResponse({
        "status": 0,
        "msg": "保存成功",
        "data": form_data
    })


@app.get("/api/users")
async def get_users():
    """获取用户数据"""
    # 模拟用户数据
    users = [
        {"id": 1, "name": "张三", "email": "zhangsan@example.com", "age": 25, "gender": "male"},
        {"id": 2, "name": "李四", "email": "lisi@example.com", "age": 30, "gender": "female"},
        {"id": 3, "name": "王五", "email": "wangwu@example.com", "age": 28, "gender": "male"},
        {"id": 4, "name": "赵六", "email": "zhaoliu@example.com", "age": 35, "gender": "female"},
    ]
    
    return JSONResponse({
        "status": 0,
        "msg": "获取成功",
        "data": {
            "items": users,
            "total": len(users)
        }
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000, reload=True)

# uvicorn example.main:app --host 0.0.0.0 --port 3000 --reload