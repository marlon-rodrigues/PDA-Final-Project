
# coding: utf-8

# In[1]:


print(sc.version)


# In[2]:


# Get Project Type that Receive most donations
dfProjectType=spark.sql("SELECT ProjectsHiveTable.`Project Type`,              SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total              from ProjectsHiveTable JOIN DonationsHiveTable ON              ProjectsHiveTable.`Project ID` = DonationsHiveTable.`Project ID`              GROUP BY ProjectsHiveTable.`Project Type`")
dfProjectType.show()


# In[3]:


# Create Hive table with results
dfProjectType.createOrReplaceTempView("ProjectTypeTempTable")
spark.sql("create table ResultsProjectTypeTable as select * from ProjectTypeTempTable")


# In[6]:


# Correlation of Teachers and Non Teachers Donations - Teachers Data
dfDonorType=spark.sql("SELECT DonorsHiveTable.`Donor is Teacher`,               SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total               FROM DonationsHiveTable JOIN DonorsHiveTable ON               DonorsHiveTable.`Donor ID` = DonationsHiveTable.`Donor ID`               GROUP BY DonorsHiveTable.`Donor is Teacher`")
dfDonorType.show()


# In[7]:


# Create Hive table with results
dfDonorType.createOrReplaceTempView("DonorTypeTempTable")
spark.sql("create table ResultsDonorTypeTable as select * from DonorTypeTempTable")


# In[8]:


# Correlation of Males and Females Teachers Donations
dfTeachersGender=spark.sql("SELECT TeachersHiveTable.`Teacher Prefix`,               SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total               FROM DonationsHiveTable JOIN TeachersHiveTable ON               TeachersHiveTable.`Teacher ID` = DonationsHiveTable.`Donor ID`               GROUP BY TeachersHiveTable.`Teacher Prefix`")
dfTeachersGender.show()


# In[9]:


# Create Hive table with results
dfTeachersGender.createOrReplaceTempView("TeachersGenderTempTable")
spark.sql("create table ResultsTeachersGenderTable as select * from TeachersGenderTempTable")


# In[11]:


# State with most make donations
dfDonationsMadeByState=spark.sql("SELECT DonorsHiveTable.`Donor State`,                                  SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total                                  FROM DonationsHiveTable JOIN DonorsHiveTable ON                                  DonorsHiveTable.`Donor ID` = DonationsHiveTable.`Donor ID`                                  GROUP BY DonorsHiveTable.`Donor State`")
dfDonationsMadeByState.show(dfDonationsMadeByState.count(), False)


# In[12]:


# Create Hive table with results
dfDonationsMadeByState.createOrReplaceTempView("DonationsMadeByStateTempTable")
spark.sql("create table ResultsDonationsMadeByStateTable as select * from DonationsMadeByStateTempTable")


# In[13]:


# State with most received donations
dfDonationsByState=spark.sql("SELECT SchoolsHiveTable.`School State`,                              SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total                              FROM DonationsHiveTable                              JOIN ProjectsHiveTable ON                              DonationsHiveTable.`Project ID` = ProjectsHiveTable.`Project ID`                              JOIN SchoolsHiveTable ON                              SchoolsHiveTable.`School ID` = ProjectsHiveTable.`School ID`                              GROUP BY SchoolsHiveTable.`School State`")
dfDonationsByState.show(dfDonationsByState.count(), False)


# In[14]:


# Create Hive table with results
dfDonationsByState.createOrReplaceTempView("DonationsByStateTempTable")
spark.sql("create table ResultsDonationsByStateTable as select * from DonationsByStateTempTable")


# In[15]:


# School Type with most received donations
dfSchoolType=spark.sql("SELECT SchoolsHiveTable.`School Metro Type`,                        SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total                        FROM DonationsHiveTable                        JOIN ProjectsHiveTable ON                        DonationsHiveTable.`Project ID` = ProjectsHiveTable.`Project ID`                        JOIN SchoolsHiveTable ON                        SchoolsHiveTable.`School ID` = ProjectsHiveTable.`School ID`                        GROUP BY SchoolsHiveTable.`School Metro Type`")
dfSchoolType.show()


# In[16]:


# Create Hive table with results
dfSchoolType.createOrReplaceTempView("SchoolTypeTempTable")
spark.sql("create table ResultsSchoolTypeTable as select * from SchoolTypeTempTable")


# In[17]:


# Project Resource category - Books vs Techonology - that Receive most donations
dfProjectResource=spark.sql("SELECT ProjectsHiveTable.`Project Resource Category`,              SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total              from ProjectsHiveTable              JOIN DonationsHiveTable ON              ProjectsHiveTable.`Project ID` = DonationsHiveTable.`Project ID`              WHERE ProjectsHiveTable.`Project Resource Category` = 'Technology'              OR ProjectsHiveTable.`Project Resource Category` = 'Books'              GROUP BY ProjectsHiveTable.`Project Resource Category`")
dfProjectResource.show()


# In[18]:


# Create Hive table with results
dfProjectResource.createOrReplaceTempView("ProjectResourceTempTable")
spark.sql("create table ResultsProjetResourceTable as select * from ProjectResourceTempTable")


# In[24]:


# Get Donations by Year
dfDonationsByYear=spark.sql("SELECT SUBSTRING(DonationsHiveTable.`Donation Received Date`, 0,4) AS DonationYear,              SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total              from DonationsHiveTable              GROUP BY DonationYear              ORDER BY DonationYear DESC")
dfDonationsByYear.show()


# In[25]:


# Create Hive table with results
dfDonationsByYear.createOrReplaceTempView("DonationsByYearTempTable")
spark.sql("create table ResultsDonationsByYearTable as select * from DonationsByYearTempTable")


# In[26]:


# Get Donations by Month/Year
dfDonationsByDate=spark.sql("SELECT SUBSTRING(DonationsHiveTable.`Donation Received Date`, 0,7) AS DonationDate,              SUM(CAST(DonationsHiveTable.`Donation Amount` AS DECIMAL(10,2))) AS Total              from DonationsHiveTable              GROUP BY DonationDate              ORDER BY DonationDate DESC")
dfDonationsByDate.show()


# In[27]:


# Create Hive table with results
dfDonationsByDate.createOrReplaceTempView("DonationsByDateTempTable")
spark.sql("create table ResultsDonationsByDateTable as select * from DonationsByDateTempTable")

