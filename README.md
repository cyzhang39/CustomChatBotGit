方法：<br>
1.读取pdf文件<br>
2.提取pdf文件中的内容<br>
3.把这些内容分成不同的部分<br>
4.把这些部分用langchain表示（embeddings）<br>
5.用户提问的时候，分析用户的问题是想要什么答案<br>
6.openai根据第五步的分析生成关于pdf相关的回答<br>

步骤：<br>
创建一个virtualenvironment, python 3.8，3.9都可以其它没试过<br>
安装包<br>
streamlit<br>
openai<br>
python-dotenv<br>
tiktoken<br>
langchain<br>
pyPDF2<br>
faiss-cpu<br>

参考：<br>
https://github.com/bnsreenu/python_for_microscopists/tree/master/323-Train%20a%20chatbot%20on%20your%20own%20documents<br>
https://github.com/alejandro-ao/ask-multiple-pdfs<br>

LangChain<br>
https://github.com/langchain-ai/langchain<br>
https://python.langchain.com/docs/use_cases/chatbots<br>
