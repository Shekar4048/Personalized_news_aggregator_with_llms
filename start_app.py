import uvicorn
if __name__ == '__main__':
    uvicorn.run('news_aggregator:app', port=8000, reload=True)