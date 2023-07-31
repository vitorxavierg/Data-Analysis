# Restricting Year column to current year
df = df[df['Year']==2022]

# Statistical Infos
df.describe()

# Nº of Records, per brand, in the Dataset
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure (figsize = (10,4))
plt.title('Cars Records')
count = sns.countplot(x=df["Brand"])
for i in count.containers:    
    count.bar_label(i,)
plt.show()

# Price's column boxplot
sns.boxplot(x=df['Price'])
plt.title('Price Boxplot', fontsize=15)
plt.show()

# Review's column boxplot
sns.boxplot(x=df['Review'])
plt.title('Reviews Boxplot', fontsize=15)
plt.show()

# Checking the number of unique values per column
df.nunique()

# Boxplot per brand
plt.figure(figsize=(20,10))
plt.title('Price Distribution of Brands', fontsize=30)
sns.boxplot(x=df['Price'], y=df['Brand'])
sns.boxplot(x=df['Price'], y=df['Brand']).set_xlabel("Price",fontsize=20)
sns.boxplot(x=df['Price'], y=df['Brand']).set_ylabel("Brand",fontsize=20)
plt.show()

# Checking Price Column distribution 
plt.figure(figsize=(10,5))
plt.title("Distribution of the Prices")
df['Price'].hist(bins=50, label='Price', alpha=0.6)
plt.axvline(np.mean(df['Price']), ls='--', c='r', label="Mean")
plt.axvline(np.median(df['Price']), ls='--', c='g', label="Median")
plt.legend()
plt.show()

# Plotting median review values, per brand
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_median_review, x='Brand', y='Review', color='lightblue')
plt.title('Review Grades (Median)')
plt.xlabel('Brand')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)

# Plotting median price values, per brand
import plotly.express as px
fig = px.line(df_median_price, x='Brand', y='Price', markers=True, text='Price', title='Median Price per Brand')
fig.update_traces(textposition='bottom right')
fig.show()   

# FIAT - Plotting median review values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_FIAT2.sort_values(by='Review', ascending=False), x='Trim Level', y='Review', color='steelblue')
plt.title('Fiat - Reviews (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)   

# FIAT - Plotting median price values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_FIAT2.sort_values(by='Price', ascending=False), x='Trim Level', y='Price', color="yellow")
plt.title('Fiat - Prices (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Price Median (U$)')
for i in median_review.containers:    
    median_review.bar_label(i,)

# Alfa Romeo - Plotting median review values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_ALFA2.sort_values(by='Review', ascending=False), x='Trim Level', y='Review', color='steelblue')
plt.title('Alfa Romeo - Reviews (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Alfa Romeo - Plotting median price values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_ALFA2.sort_values(by='Price', ascending=False), x='Trim Level', y='Price', color='yellow')
plt.title('Alfa Romeo - Price Values (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Price Median (U$)')
for i in median_review.containers:    
    median_review.bar_label(i,)
    
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Jeep - Plotting median review values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_JEEP2.sort_values(by='Review', ascending=False), x='Trim Level', y='Review', color='steelblue')
plt.title('Jeep - Reviews (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Jeep - Plotting median price values, per Trim Level
plt.figure(figsize=(15,4))
median_review = sns.barplot(data=df_JEEP2.sort_values(by='Price', ascending=False), x='Trim Level', y='Price', color='yellow')
plt.title('Jeep - Price Values (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Price Median (U$)')
for i in median_review.containers:    
    median_review.bar_label(i,)
    
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Chrysler - Plotting median review values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_CHRYSLER2.sort_values(by='Review', ascending=False), x='Trim Level', y='Review', color='steelblue')
plt.title('Chrysler - Reviews (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Chrysler - Plotting median price values, per Trim Level
plt.figure(figsize=(15,4))
median_review = sns.barplot(data=df_CHRYSLER2.sort_values(by='Price', ascending=False), x='Trim Level', y='Price', color='yellow')
plt.title('Chrysler - Price Values (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Price Median (U$)')
for i in median_review.containers:    
    median_review.bar_label(i,)
    
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Mercedes-Benz - Plotting median review values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_MERCEDES2.sort_values(by='Review', ascending=False), x='Trim Level', y='Review', color='steelblue')
plt.title('Mercedes-Benz - Reviews (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)
for item in median_review.get_xticklabels():
    item.set_rotation(90)

# Mercedes-Benz - Plotting median price values, per Trim Level
plt.figure(figsize=(15,4))
median_review = sns.barplot(data=df_MERCEDES2.sort_values(by='Price', ascending=False), x='Trim Level', y='Price', color='yellow')
plt.title('Mercedes-Benz - Price Values (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Price Median (U$)')
for i in median_review.containers:    
    median_review.bar_label(i,)
    
for item in median_review.get_xticklabels():
    item.set_rotation(90)

# Honda - Plotting median review values, per Trim Level
plt.figure(figsize=(15,5))
median_review = sns.barplot(data=df_HONDA2.sort_values(by='Review', ascending=False), x='Trim Level', y='Review', color='steelblue')
plt.title('Honda - Reviews (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Review Median')
for i in median_review.containers:    
    median_review.bar_label(i,)
for item in median_review.get_xticklabels():
    item.set_rotation(45)

# Honda - Plotting median price values, per Trim Level
plt.figure(figsize=(15,4))
median_review = sns.barplot(data=df_HONDA2.sort_values(by='Price', ascending=False), x='Trim Level', y='Price', color='yellow')
plt.title('Honda - Price Values (Median) x Trim Level')
plt.xlabel('Trim Level')
plt.ylabel('Price Median (U$)')
for i in median_review.containers:    
    median_review.bar_label(i,)
    
for item in median_review.get_xticklabels():
    item.set_rotation(45)