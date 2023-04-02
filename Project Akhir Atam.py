


# ## Import Data

# In[114]:


df = pd.read_excel (r'C:\Users\Atam Rifai S\OneDrive - ITPLN\OneDrive - Komputer\Script\Machine Learning\Dicoding\Dicoding Submission\Ekspor Ikan Kabupaten Situbondo 2016-2017.xls')
df


# ## Melihat informasi Data

# In[24]:


df.info()


# In[28]:


Plottidf.describe()


# ## Plotting Data Hasil Import

# In[26]:


f1 = df["TON"].values
f2 = df["RP (000)"].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='Blue')


# # Algoritma Clustering dengan Algoritma Euclidean Distance

# ### Membuat rumus Algoritma Euclidean Distance

# In[30]:


def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)


# In[38]:


k = 3
C = X[0:3]
plt.scatter(f1, f2, c="#5ab0c7")
plt.scatter(C[:,0], C[:,1], marker="*", s=100, c='g')


# ### Membuat Area Clustering

# In[39]:


C_old = np.zeros(C.shape)

clusters = np.zeros(len(X))

error = dist(C, C_old, None)

count = 1
while (error !=0):
    for i in range(len(X)):
        distances = dist(X[i],C)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    
    C_old = deepcopy(C)
    
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j]==i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, C_old, None)


# In[104]:


colors = ['r', 'y', 'g']
fig, ax = plt.subplots()
for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=300, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=300, c='#050505')

hasil = np.array(list(zip(df["Jenis Ikan"], clusters)))


# ## Output Clustering dengan Euclidean

# ### Mengelempokkan hasil clustering berdasarkan jenis ikan
# 

# In[103]:


hasil = ('Jenis Ikan', df["Jenis Ikan"].values), ('Cluster', clusters)
hasil


# In[106]:


output = ['Layang', 'Kembung', 'Kerapu', 'Tongkol', 'Tengiri', 'Bambangan',
                'Selar', 'Teri', 'Lemuru', 'Layur', 'Petek', 'Cucut', 'Manyung',
                'P a r i', 'Beloso', 'Udang Lainnya', 'Kakap', 'Kurisi', 'Lainnya',
                'Cumi-Cumi', 'Bawal putih', 'Belanak', 'Rajungan', 'Beronang',
                'Kepiting'],[0., 1., 2., 0., 1., 2., 1., 1., 1., 1., 1., 1., 1., 1., 1., 2., 2.,
         1., 1., 1., 1., 1., 1., 1., 1.]


# ### Menampilkan Output Hasil Clustering

# In[108]:


df1 = pd.DataFrame (output).transpose()
df1.columns = ['Jenis Ikan', 'Cluster']
print(df1)


# # Klustering K-Means Scikir Learn

# In[115]:


df


# In[119]:


ikan_x = df.iloc[:, 1:3]
ikan_x.head()


# In[120]:


x_array = np.array(ikan_x)
print(x_array)


# In[122]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)
x_scaled


# In[124]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, random_state=123)


# In[125]:


kmeans.fit(x_scaled)


# In[126]:


print(kmeans.cluster_centers_)


# In[128]:


df["kluster"] = kmeans.labels_


# In[129]:


output = plt.scatter(x_scaled[:,0], x_scaled[:,1], s = 100, c = df.kluster, marker = "o", alpha = 1, )
centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='red', s=200, alpha=1 , marker="o");
plt.title("Hasil Klustering K-Means")
plt.colorbar(output)
plt.show()


# # Kesimpulan

# Dari penggunaan 2 algoritma dengan scikitlearn import K-Means dan dengan mendifinisikan algoritma Euclidiean distance sendiri hasilnya adalah sama sama memiliki ouutput yang sama
# 
