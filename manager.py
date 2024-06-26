if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="src.app.main:app_factory",
        host="0.0.0.0",
        port=8001,
        reload=True,
        factory=True,
        workers=1,
    )
