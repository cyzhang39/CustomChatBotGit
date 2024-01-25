方法：<br>
1.读取pdf文件
2.提取pdf文件中的内容
3.把这些内容分成不同的部分
4.把这些部分用langchain表示（embeddings）
5.用户提问的时候，分析用户的问题是想要什么答案
6.openai根据第五步的分析生成关于pdf相关的回答

步骤：
创建一个virtualenvironment, python 3.8，3.9都可以其它没试过
安装包
streamlit
openai
python-dotenv
tiktoken
langchain
pyPDF2
faiss-cpu

参考：
https://github.com/bnsreenu/python_for_microscopists/tree/master/323-Train%20a%20chatbot%20on%20your%20own%20documents
https://github.com/alejandro-ao/ask-multiple-pdfs

LangChain
https://github.com/langchain-ai/langchain
https://python.langchain.com/docs/use_cases/chatbots
