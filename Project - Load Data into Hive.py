
# coding: utf-8

# In[1]:


print(sc.version)


# In[4]:


# Load Teachers Data
dfTeachers = spark.read.csv("hdfs://localhost:54310/user/hduser/project/Teachers.csv", header=True, sep=',', inferSchema=True)
dfTeachers.printSchema()


# In[6]:


dfTeachers.show()


# In[7]:


# Load Schools Data
dfSchools = spark.read.csv("hdfs://localhost:54310/user/hduser/project/Schools.csv", header=True, sep=',', inferSchema=True)
dfSchools.printSchema()


# In[8]:


dfSchools.show()


# In[9]:


# Load Donors Data
dfDonors = spark.read.csv("hdfs://localhost:54310/user/hduser/project/Donors.csv", header=True, sep=',', inferSchema=True)
dfDonors.printSchema()


# In[10]:


dfDonors.show()


# In[11]:


# Load Donations Data
dfDonations = spark.read.csv("hdfs://localhost:54310/user/hduser/project/Donations.csv", header=True, sep=',', inferSchema=True)
dfDonations.printSchema()


# In[12]:


dfDonations.show()


# In[14]:


# Load Projects Data
dfProjects = spark.read.csv("hdfs://localhost:54310/user/hduser/project/Projects.csv", header=True, sep=',', inferSchema=True)
dfProjects.printSchema()


# In[11]:


dfProjects.show()


# In[15]:


# Create Temp Tables from CSVs
dfTeachers.createOrReplaceTempView("TeachersTempTable")
dfSchools.createOrReplaceTempView("SchoolsTempTable")
dfDonors.createOrReplaceTempView("DonorsTempTable")
dfDonations.createOrReplaceTempView("DonationsTempTable")
dfProjects.createOrReplaceTempView("ProjectsTempTable")


# In[16]:


# Create Hive Tables from Temp Tables
spark.sql("create table TeachersHiveTable as select * from TeachersTempTable")
spark.sql("create table SchoolsHiveTable as select * from SchoolsTempTable")
spark.sql("create table DonorsHiveTable as select * from DonorsTempTable")
spark.sql("create table DonationsHiveTable as select * from DonationsTempTable")
spark.sql("create table ProjectsHiveTable as select * from ProjectsTempTable")

