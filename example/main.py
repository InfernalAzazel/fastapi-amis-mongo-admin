from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi_amis_admin.amis.function.app import AApp


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    amis_app = AApp()
    amis_app.type = 'app'
    amis_app.brandName = "FastAPI Amis Example"
    amis_app.logo = "https://suda.cdn.bcebos.com/images%2F2021-01%2Fdiamond.svg"
    
    # 配置页面
    amis_app.pages = [
        {
            "label": "表单示例",
            "icon": "fa fa-edit",
            "url": "/",
            "schema": {
                "type": "page",
                "title": "表单示例",
                "body": {
                    "type": "form",
                    "mode": "horizontal",
                    "api": "/saveForm",
                    "body": [
                        {
                            "label": "姓名",
                            "type": "input-text",
                            "name": "name",
                            "required": True
                        },
                        {
                            "label": "邮箱",
                            "type": "input-email",
                            "name": "email",
                            "required": True
                        },
                        {
                            "type": "submit",
                            "label": "提交",
                            "level": "primary"
                        }
                    ]
                }
            }
        }
    ]

    return HTMLResponse(content=amis_app.render())


@app.post("/saveForm")
async def save_form():
    """处理表单提交"""
    return {
        "status": 0,
        "msg": "表单提交成功！",
        "data": {}
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000, reload=True)

# uvicorn example.main:app --host 0.0.0.0 --port 3000 --reload