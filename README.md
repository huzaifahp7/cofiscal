<div align="center">
  <br>
  <h1>CoFiscal 🪙</h1>
  <strong>Guiding your financial future, one loan at a time!</strong>
</div>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTI2ZmppZGZveWZ1am55a3J2OXhmdnM3M29sdXFueWo3eHhqc3NneiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bMycGOQLESDCEnLNUz/giphy.gif" alt="CoFiscal GIF">
</p>

## 💻 **Repository Structure**
Currently all our various components are present in the branches (frontend, backend, flask etc.). Simply navigate to a branch to view the associated code. If you wish to run that particular, instructions for installation and deployment exist in the respective branch's readme.

## 💰 **Inspiration**
CoFiscal was born from a realization that there existed a significant gap in the market—an alarming lack of accessible information and education for individuals considering loans, leading to uninformed financial decisions, which directly impacted the default rates. This insight emerged during the ideation process when we delved into financial data and lending statistics.

The statistics revealed that up to 35% of loan applicants had limited knowledge of their credit scores, leading to suboptimal loan decisions and higher default rates. It became evident that informed borrowers have a better chance of securing loans that align with their financial capacity and objectives.

Upon the conceptualization of CoFiscal, our vision was to empower borrowers with data-driven insights, helping them make informed decisions and reduce the likelihood of default. This will result in fewer borrowers defaulting and assist banks in mitigating losses, improving loan performance, enhancing portfolio quality, and producing targeted loan schemes.

## Getting Started

The project relies on several Python libraries for its functionality. These dependencies are specified in the `requirements.txt` file. 

To set up your development environment and install all these dependencies, follow the steps below:

1. Ensure you have Python and `pip` installed on your machine.
2. Navigate to the root directory of the project using your terminal or command prompt.
3. Run the following command:

```bash
pip install -r requirements.txt

Next, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

# Table of Contents

1. [What it does](#what-it-does)
2. [How we built it](#how-we-built-it)
3. [Challenges we ran into](#challenges-we-ran-into)
4. [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
5. [What we learned](#what-we-learned)
6. [What's next for CoFiscal](#whats-next-for-cofiscal)


## ⚙️ **What it does**
CoFiscal is a cutting-edge financial platform that leverages advanced AI models to perform in-depth analyses of your financial profile. We break down your financial data to offer you insights and guidance, helping you make informed decisions about loans. We're essentially your financial navigator, providing a roadmap to safer and smarter borrowing choices. With CoFiscal, you can confidently embark on your financial journey, knowing that your future is being thoughtfully considered and protected.

## 🛠️ **How we built it**
**Programming Languages:** Python was chosen for its versatility in handling data preprocessing, machine learning, and integrating various components.

**Machine Learning Models:** LightGBM implemented from sklearn was employed for its efficiency in gradient boosting, making it a suitable choice for predicting loan default probabilities.

**Data Preprocessing:** NumPy, RegEx and Pandas libraries were essential for data preprocessing, including tasks such as data cleaning, feature engineering, and handling numerical data.

**Over-sampling Technique:** To tackle the significant data skewness issue in the dataset, SMOTE (Synthetic Minority Over-sampling Technique) was used to generate synthetic data points for the minority class, ultimately balancing the dataset. This was crucial in improving model performance on unseen data.\
\
**Front-end Development:** The front-end was built using React for creating user interfaces and Next.js for server-side rendering. This combination provided a robust, interactive, and SEO-friendly user experience.\
\
**Web Framework:** As a micro web framework for Python, Flask played a pivotal role in building the back end. It handled routing, HTTP requests, and served as the connection point between the front end and the machine learning model. Flask ensured seamless communication between different components. Libraries such as JSON were vital for the successful running of Flask.\
\
**OCR (Optical Character Recognition):** pdfminer.six was used for OCR, enabling the recognition of text in images and PDFs. PyPDF2 was employed to extract text from PDF files, enhancing OCR processing. This feature helped autofill user input features by reading credit reports.\
\
**LLM (Large Language Model):** The Zero-Shot LLM PaLM API from google.generativeai was manually trained using Few-Shot Learning techniques. This was integrated to provide users with valuable insights based on their loan default probabilities such as why they should or should not take that specific loan, and general financial tips on loans. Users could make informed decisions based on these insights.\
\
**Data Set:** Kaggle's Loan Default Dataset, containing 250,000 data points, was used for both training and testing the machine learning model. Over-sampling techniques were applied to address data imbalance.\
\
**Version Control:** Collaborative development and version control were managed using Git, allowing the team to work seamlessly on the project and keep track of code changes.\
\
**Testing and Evaluation:** The model was rigorously tested with 500 epochs, and its performance was evaluated on both seen and unseen data. This comprehensive testing resulted in the reported accuracy, precision, recall, and F1 scores.

<img src = 'https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/python2.png' height='30'/>  <img src = 'https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/html.svg' width='30'/> <img src='https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/java.svg' width='30'/>
<img src = 'https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/css.svg' width='30'/> <img src = 'https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/js.svg' width='30'/> 

## ⛔ **Challenges we ran into**
**Skewed Dataset:** The dataset we used was heavily skewed, with 98% of entries representing loans that did not default, making model accuracy appear high (88%) on seen data but resulting in very low accuracy (15%) on unseen data.\
\
**Under-sampling Difficulty:** Attempting to address data skewness by undersampling "not defaulted" entries to match "defaulted" entries proved ineffective, as it was insufficient to overcome the skewed nature of the dataset, especially given the decision-tree-based classification model we were using.\
\
**OCR Data Extraction:** Our OCR feature, while essential for user convenience, struggled to automatically extract input features and identify data variables. Credit reports did not explicitly mention the features, necessitating additional coding to handle such calculations, like income, and correctly identify the variables.\
\
**Integration Challenges:** Connecting the OCR feature with Flask, our web framework, presented technical hurdles due to compatibility issues between libraries. This challenge required careful debugging and troubleshooting.\
\
**Front-end Integration:** We encountered difficulties connecting the front-end with Flask, particularly because none of the team members were Flask experts. This integration issue demanded significant time and effort to resolve.

## 🏆 **Accomplishments that we're proud of**
**Data Skewness Tackled:** Our solution to the extreme data skewness, through Synthetic Minority Over-sampling Technique (SMOTE), not only balanced the dataset but also significantly improved model performance. By generating synthetic data points for the minority class, we made the model more resilient to unseen data.\
\
**OCR Enhancement:** Our dedication to optimizing the OCR feature sets us apart. We invested time and effort to develop custom code that could interpret credit reports and extract essential user input features accurately. This improvement made the OCR feature highly robust and reduced the likelihood of user input errors.\
\
**Machine Learning Excellence:** Achieving an impressive 92.03% accuracy on unseen data using the LightGBM model is a testament to our commitment to excellence in machine learning. We leveraged 500 epochs to fine-tune the model and delivered exceptional results, boasting precision, recall, and F1 score well above industry standards.\
\
**Empowering Financial Decision-Making:** We take pride in providing users with a powerful tool to make informed financial decisions. By predicting their probability of loan default and offering insights through PaLM API, we help users secure their financial future.\
\
**Front-end Excellence with React, Next.js, and Flask Expertise:** We've combined the power of React, Next.js, and Flask to create a visually stunning and user-friendly front-end. Through dedication and learning, we overcame initial challenges in connecting the front end to Flask, ensuring seamless integration and improved user interaction.

## 📝 What we learned
**Data Skewness Understanding:** We gained a deep understanding of the significance of data skewness in machine learning models. Recognizing the importance of balanced datasets, we realized that the accuracy metric alone might not reflect model performance accurately.\
\
**Data Preprocessing Techniques:** Our experience with Synthetic Minority Over-sampling Technique (SMOTE) was enlightening. We learned how this oversampling technique could effectively address class imbalance issues, making our model more robust.\
\
**Model Selection:** We gained a fine understanding on the process of choosing an apt model to meet the requirements of our dataset, the idea as well as parameters such as run-time, accuracy, precision, and recall. After testing of models such as Random forest, XGBoost and DBscan, we finalized on using the LightGBM model to predict default probability.\
\
**Customization for OCR:** Enhancing the OCR data extraction process involved gaining expertise in credit report interpretation and user input extraction. This experience showed us the value of tailoring solutions to specific data types and user needs.\
\
**Dependency Management:** We learned that careful review and management of library dependencies are essential for seamless integration between different components of the project. This experience emphasized the significance of thorough testing and compatibility checks.\
\
**Front-end Integration:** Overcoming front-end challenges through teamwork and learning was an invaluable experience. Seeking guidance from various documentations and investing time in understanding the Flask framework improved our problem-solving skills and ability to handle similar issues effectively in the future.

## 🛫 What's next for CoFiscal
The next step in the growth of CoFiscal is the implementation of the following features that we have planned, making it more holistic and feature-heavy for both the banks and borrowers:

**Market Information:** This is a feature that is going to scrape reliable financial news websites and filter the information to provide the borrowers with valuable loan-related information about the market and whether it is the best time to take loans. It would be an addition, helping further educate the borrower in making smarter financial decisions.

**Simulator:** This would be assistance provided on the website wherein the user would be able to toggle the interest rate, loan term and loan amount and get the probability of defaulting in order to help them find the range of loans that are best suited for them. This would be a dynamic feature which would mean that all the updation of the variables and generation of the prediction happens in real time.

**Loan Recs:** This is another feature that would provide the user with all the available loans providers and the information that the bank provides about the load in order to have a collection of all options for the user which they can choose from in case of searching for loans.

**Improved OCR:** This is improving existing functionality to accept more kinds of pdf and scrape all the data possible from the document in order to simplify and make the user interaction with the website easier.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌐 Devpost
For a deeper dive into our journey and the creation of CoFiscal, check out our story on [Devpost](https://devpost.com/software/cofiscal)!

[![Devpost](https://img.shields.io/badge/Our%20Story%20on-Devpost-blue?logo=devpost&style=for-the-badge)](https://devpost.com/software/cofiscal)

## 🚀 Our Team

We're a group of passionate developers working together to make a difference. Meet our team:

- **Farzad Ashfak** - [![GitHub](https://img.shields.io/badge/GitHub-FarzadAshfak-blue?logo=github&style=flat-square)](https://github.com/farzadashfak)
- **Huzaifa Pardawala** - [![GitHub](https://img.shields.io/badge/GitHub-HuzaifahP7-blue?logo=github&style=flat-square)](https://github.com/huzaifahp7)
- **Ayush Gharat** - [![GitHub](https://img.shields.io/badge/GitHub-AyushGharat-blue?logo=github&style=flat-square)](https://github.com/ayushgharat)
- **Aditya Bajoria** - [![GitHub](https://img.shields.io/badge/GitHub-BajoAdi-blue?logo=github&style=flat-square)](https://github.com/Bajo-Adi)

Feel free to check out our profiles and connect with us!

