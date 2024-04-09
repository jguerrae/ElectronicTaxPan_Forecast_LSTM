# Predicting Electronic VAT Collection in Panama

## Authors
Juan Camilo Díaz and Jorge Guerra, in collaboration with the Financial Innovation and Macroeconomic Stability in Latin America and the Caribbean (FISLAC) initiative, part of the Inter-American Development Bank (BID).

## Description
This repository presents the project "Predicting Electronic VAT Collection in Panama," a pivotal component of the [Financial Innovation and Macroeconomic Stability in Latin America and the Caribbean (FISLAC) initiative](https://www.fislac.com/), which aims to provide a comprehensive overview of macro-fiscal risks faced by countries in the LAC region. Through an innovative blend of SARIMAX and LSTM models, this study analyzes 1.2 million data points to forecast weekly electronic VAT collections, enhancing fiscal planning and risk management. The project stands out as a testament to the power of combining statistical and deep learning approaches to tackle complex economic forecasting challenges. More about FISLAC can be found at [FISLAC](https://www.fislac.com/) and its [LinkedIn Group](https://www.linkedin.com/groups/12966860/).


## Methodology
This project addresses the challenge of predicting electronic VAT collection in Panama, utilizing an extensive dataset of 1.2 million records. The aim was to model and forecast tax collection accurately to aid fiscal planning and management. Given the volume and temporal nature of the data, an initial processing step transformed daily records into weekly aggregates. This approach not only simplified the analysis but also aligned the predictions with weekly decision-making cycles relevant for fiscal management.

To tackle this issue, a bifurcated modeling strategy was developed that captures both long-term trends and short-term fluctuations in tax collection data. Firstly, a SARIMAX model was implemented, an advanced time series approach that incorporates components of auto-regression, differentiation, and moving averages, along with seasonal and exogenous effects. This model was specifically designed to capture the underlying trend in the data, enabling an understanding of how electronic VAT collection could evolve in the long term under various conditions.

In parallel, an LSTM (Long Short-Term Memory) neural network was used to model short-term variations. LSTM networks are particularly suited for this purpose due to their ability to learn long-term temporal dependencies, making them ideal for capturing the complex dynamics and hidden patterns in financial time series. The integration of this model allowed for the fine-tuning of weekly predictions, adjusting for sudden changes and non-linear patterns that the SARIMAX model might not fully capture.

The combination of these two approaches provided a robust and comprehensive solution for predicting electronic VAT collection in Panama. The transformation of data into a weekly format, along with modeling long-term trends and short-term variations, offered a detailed and nuanced view of fiscal behavior. This project demonstrates the effectiveness of combining statistical models and deep learning to analyze and predict complex economic phenomena, facilitating better planning and data-driven decision-making.

## License
This project is licensed under the MIT License, allowing its use, modification, and distribution under certain conditions.

### Contact
For questions or collaborations, please contact [Jorge Guerra](mailto:ja.guerrae@uniandes.edu.co)


## License
This project is licensed under the MIT License, permitting its use, modification, and distribution under specific terms.

### Contact
For inquiries or partnership opportunities, please contact [Juan Camilo Díaz](mailto:contact@fislac.com).
