import streamlit as st
if "show_details" not in st.session_state:
    st.session_state.show_details = False
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'],errors='coerce')
st.sidebar.title('Startup Funding Analysis')

def load_overall_analysis():
    st.title('Overall Analysis')
    col1,col2,col3,col4 = st.columns(4)
    #total investested money till in indian startups
    with col1:
        total_amount = round(df['amount'].sum())
        st.metric('Total Amount', str(total_amount) + 'cr')

    #maximum investment
    with col2:
        max_investment = round(df['amount'].max())
        st.metric('Max Investment', str(max_investment) + 'cr')

    #for average
    with col3:
        average = round(df['amount'].mean())
        st.metric('Average funding', str(average) + 'cr')

    with col4:
       no_startup = df['startup'].nunique()
       st.metric('Number of Startups', str(no_startup) )

    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    st.header('MOM graph')
    selected_option = st.selectbox('select Type',['Total','Count'])
    if selected_option == 'Total':

        temp_df = df.groupby(['month','year'])['amount'].sum().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

        fig5, ax5 = plt.subplots()
        ax5.plot(temp_df['x_axis'],temp_df['amount'])

        st.pyplot(fig5)
    else :
        temp_df = df.groupby(['month', 'year'])['amount'].count().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

        fig6, ax6 = plt.subplots()
        ax6.plot(temp_df['x_axis'], temp_df['amount'])

        st.pyplot(fig6)
    col1, col2 = st.columns(2)
    with col1:
        top_sector = df.groupby('vertical')['amount'].count().sort_values(ascending=False).head()
        st.subheader('top five most no of startups sectors in pie chart')

        fig7, ax7 = plt.subplots()
        ax7.pie(top_sector, labels=top_sector.index, autopct='%1.1f%%')

        st.pyplot(fig7)

    with col2:
        top_sector1 = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('top five most valuable sectors in pie chart')

        fig8, ax8 = plt.subplots()
        ax8.pie(top_sector1, labels=top_sector1.index, autopct='%1.1f%%')

        st.pyplot(fig8)
    st.header('Types of Funding Basic on Money and how many startups')

    col1, col2 = st.columns(2)
    with col1:
        rounds_count = df.groupby('round')['vertical'].count().sort_values(ascending=False).head(10)
        st.subheader('Best Funding Type')
        fig9, ax9 = plt.subplots(figsize =(15,9))
        ax9.bar(rounds_count.index, rounds_count.values)
        ax9.set_xlabel('Funding Types')
        ax9.set_ylabel('Number of startups')

        plt.xticks(rotation=45,ha='right')
        plt.tight_layout()

        st.pyplot(fig9)

    with col2:
        rounds_sum = df.groupby('round')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader('Best Funding level of amount')
        fig10, ax10 = plt.subplots(figsize=(15, 9))
        ax10.bar(rounds_sum.index, rounds_sum.values)
        ax10.set_xlabel('Funding Types')
        ax10.set_ylabel('amount of invest')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        st.pyplot(fig10)

    st.header('analysis basic on the city')
    col1, col2 = st.columns(2)
    with col1:
        city_count = df.groupby('city')['startup'].count().sort_values(ascending=False).head(10)
        st.subheader('Best city for startups')
        fig11, ax11 = plt.subplots(figsize=(15, 9))
        ax11.bar(city_count.index, city_count.values)
        ax11.set_xlabel('city name')
        ax11.set_ylabel('no of startups')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        st.pyplot(fig11)

    with col2 :
        city_sum = df.groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader('Best city for startups by level of amount')
        fig12, ax12 = plt.subplots(figsize=(15, 9))
        ax12.bar(city_sum.index, city_sum.values)
        ax12.set_xlabel('city name')
        ax12.set_ylabel('Amount of invest in city')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        st.pyplot(fig12)

    st.header("Top Investor on the Two Basis")
    col1, col2 = st.columns(2)
    with col1:

        investor_count = df.groupby('investors')['startup'].count().sort_values(ascending=False).head(10)
        st.subheader('Top investors basic of numbers')
        fig12, ax12 = plt.subplots(figsize=(15, 9))
        ax12.bar(investor_count.index, investor_count.values)
        ax12.set_xlabel('investor name')
        ax12.set_ylabel('no of startups invest')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        st.pyplot(fig12)

    with col2:

        investor_sum = df.groupby('investors')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader('Top investors basic on the amount')
        fig12, ax12 = plt.subplots(figsize=(15, 9))
        ax12.bar(investor_sum.index, investor_sum.values)
        ax12.set_xlabel('investor name')
        ax12.set_ylabel('Amount invest in startups')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        st.pyplot(fig12)

    st.header('Top startups Year wise')
    selected_year = st.selectbox('select Type', [2015,2016,2017,2018,2019,2020])
    st.subheader('for find top 5 best startups')
    def year_best_st(selected_year):
        year_wise_best =  df[df['year'] == selected_year][['startup', 'amount']].sort_values(by='amount', ascending=False).head(10)

        return st.dataframe(year_wise_best)
    year_best_st(selected_year)

    st.subheader('all money invest in this year')

    def year_best_st1(selected_year):
        Total_amount = round(df[df['year'] == selected_year][['startup', 'amount']]['amount'].sum())
        return st.metric('Total Amount', str(Total_amount) + 'cr')
    year_best_st1(selected_year)

def load_startup_details(startup):
    st.title(startup)
    last5_df = df[df['startup'].str.contains(startup)].head()[
        ['startup', 'vertical','subvertical', 'city', 'round','date','investors','amount']]
    st.subheader('startup detials')
    st.dataframe(last5_df)

    st.header('similar companies')
    option1 = st.selectbox('select one',['city','amount'])

    if option1 == 'city':
        selected_city = st.selectbox('select one city', sorted(df['city'].unique().tolist()))
        load_similar_city(selected_city)

    if option1 == 'amount':
        st.title('similar company basis on amount')
        range_amount = st.selectbox('select one range',['1-5','5-20','20-100','100-1000'])
        lower_range_amount = int(range_amount.split('-')[0])
        upper_range_amount = int(range_amount.split('-')[1])
        load_amount_basis(lower_range_amount,upper_range_amount)


def load_amount_basis(lower_range_amount,upper_range_amount):
    st.subheader('similar companies')
    load5 = df[(df['amount'] >= lower_range_amount) & (df['amount'] <= upper_range_amount)][['date', 'startup', 'vertical', 'city', 'investors', 'round', 'amount']].head(5)
    st.dataframe(load5)



def load_similar_city(city):
    st.title(city)
    st.subheader('similar companies')
    load_5 = df[df['city'].str.contains(city)].head(5)[['round', 'amount', 'startup', 'date', 'investors', 'vertical']]
    st.dataframe(load_5)


def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('most five investments')
    st.dataframe(last5_df)


    col1, col2 = st.columns(2)
    with col1:
        # load the biggest top 5 investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('top five biggest investments')
        st.dataframe(big_series)
        #made a graph of big investments
        st.subheader('Biggest investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)

        st.pyplot(fig)
    with col2:
        st.subheader('pi chart for sector investments')
        vertical = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()

        fig1, ax1 = plt.subplots()
        ax1.pie(vertical,labels=vertical.index,autopct='%1.1f%%')

        st.pyplot(fig1)

    col3,col4 = st.columns(2)
    with col3:
        st.subheader('pi chart for stage investments')
        rounds = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()

        fig2, ax2 = plt.subplots()
        ax2.pie(rounds, labels=rounds.index, autopct='%1.1f%%')

        st.pyplot(fig2)

    with col4:
        st.subheader('pi chart for city')
        city = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()

        fig3, ax3 = plt.subplots()
        ax3.pie(city, labels=city.index, autopct='%1.1f%%')

    st.subheader('yoy graph for every investments')
    df['year'] = df['date'].dt.year
    year = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    fig4, ax4 = plt.subplots()
    ax4.plot(year.index, year.values)
    st.pyplot(fig4)



option = st.sidebar.selectbox('select one',['overall Analysis','Startup','Investor'])

if option == 'overall Analysis':
    load_overall_analysis()

elif option == 'Startup':
    selected_startup = st.sidebar.selectbox('Select startup',df['startup'].unique().tolist())
    btn1 = st.sidebar.button('startup details')
    st.title('startup Analysis')
    if btn1:
        st.session_state.show_details = True

    if st.session_state.show_details:
        st.subheader('startup details')
        load_startup_details(selected_startup)



elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('select investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Invertors details')
    if btn2:
        load_investor_details(selected_investor)






