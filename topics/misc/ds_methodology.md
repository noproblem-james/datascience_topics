# Data Science Methodologies

## Cross-Industry Process for Data Mining
CRISP-DM methodology is a process aimed at increasing the use of data mining over a wide variety of business applications and industries. The intent is to take case specific scenarios and general behaviors to make them domain neutral.  CRISP-DM is comprised of six steps with an entity that has to implement in order to have a reasonable chance of success. The six steps are shown in the following diagram:

![CRISP DM Diagram](../../images/CRISP-DM_Process_Diagram.png)

1. **Business Understanding** This stage is the most important because this is where the intention of the project is outlined. Foundational Methodology and CRISP-DM are aligned here. It requires communication and clarity. The difficulty here is that stakeholders have different objectives, biases, and modalities of relating information. They don’t all see the same things or in the same manner. Without clear, concise, and complete perspective of what the project goals are resources will be needlessly expended. 
2. **Data Understanding Data** understanding relies on business understanding. Data is collected at this stage of the process. The understanding of what the business wants and needs will determine what data is collected, from what sources, and by what methods. CRISP-DM combines the stages of Data Requirements, Data Collection, and Data Understanding from the Foundational Methodology outline. 
3. **Data Preparation** Once the data has been collected, it must be transformed into a useable subset unless it is determined that more data is needed. Once a dataset is chosen, it must then be checked for questionable, missing, or ambiguous cases. Data Preparation is common to CRISP-DM and Foundational Methodology. 
4. **Modeling** Once prepared for use, the data must be expressed through whatever appropriate models, give meaningful insights, and hopefully new knowledge. This is the purpose of data mining: to create knowledge information that has meaning and utility. The use of models reveals patterns and structures within the data that provide insight into the features of interest. Models are selected on a portion of the data and adjustments are made if necessary. Model selection is an art and science. Both Foundational Methodology and CRISP-DM are required for the subsequent stage. 
5. **Evaluation** The selected model must be tested. This is usually done by having a pre-selected test, set to run the trained model on. This will allow you to see the effectiveness of the model on a set it sees as new. Results from this are used to determine efficacy of the model and foreshadows its role in the next and final stage. 
6. **Deployment** In the deployment step, the model is used on new data outside of the scope of the dataset and by new stakeholders. The new interactions at this phase might reveal the new variables and needs for the dataset and model. These new challenges could initiate revision of either business needs and actions, or the model and data, or both.
CRISP-DM is a highly flexible and cyclical model. Flexibility is required at each step along with communication to keep the project on track. At any of the six stages, it may be necessary to revisit an earlier stage and make changes.

## Elaborated Methodology
[Slides](https://www.slideshare.net/JohnBRollinsPhD/foundational-methodology-for-data-science)
[Blog](https://web.archive.org/web/20200414234519/https://www.ibmbigdatahub.com/blog/why-we-need-methodology-data-science)

￼![alternative data science methodology](/../../images/alternative_ds_methodology.png)

the chosen analytic approach determines the data requirements. Different methods require certain data content, formats and representations, guided by domain knowledge.
Data Requirements stage of the data science methodology involves identifying the necessary data content, formats and sources for initial data collection.
When collecting data, it is alright to defer decisions about unavailable data, and attempt to acquire it at a later stage.
Data Collection stage, the data requirements are revised and decisions are made as to whether or not more data is needed.
Descriptive statistics and visualization  can be applied to the data set to assess the content, quality, and initial insights about the data.
Data Understanding: Is the data that you collected representative of the problem to be solved?  Iterative. Can loop back to data collection.
Data Preparation: addresses missing or invalid values and removes duplicates, and ensures that everything is properly  Feature engineering is the process of using domain knowledge of the data to create features. Very time-consuming can be automated
Modeling: build models that are either descriptive or predictive. play around with different algorithms to ensure  that the variables in play are actually required

An example of a descriptive model might examine things like: if a person did this,
then they're likely to prefer that.
A predictive model tries to yield yes/no, or stop/go type outcomes.
These models are based on the analytic approach that was taken, either statistically driven
or machine learning driven. play around with different algorithms to ensure
that the variables in play are actually required

Evaluation: Evaluation allows the quality of the model to be assessed but it's also an opportunity
to see if it meets the initial request.
Evaluation answers the question: Does the model used really answer the initial question
or does it need to be adjusted?
Model evaluation can have two main phases.
The first is the diagnostic measures phase, which is used to ensure the model is working
as intended. The second phase of evaluation that may be used is statistical significance testing.
This type of evaluation can be applied to the model to ensure that the data is being
properly handled and interpreted within the model

Deployment
While a data science model will provide an answer, the key to making the answer relevant
and useful to address the initial question, involves getting the stakeholders familiar
with the tool produced.
In a business scenario, stakeholders have different specialties that will help make
this happen, such as the solution owner, marketing, application developers, and IT administration.

Feedback: the more you know, the more that you'll
want to know.
iterative, ensuring the refinement at each stage in the game.
John Rollins, IBM
Your success within the data science field depends on your ability to apply the right
tools, at the right time, in the right order, to the address the right problem.

the true meaning of a methodology!
That its purpose is to explain how to look at a problem, work with data in support of
solving the problem, and come up with an answer that addresses the root problem.
