from sklearn.compose import ColumnTransformer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer,SimpleImputer,MissingIndicator
from sklearn.preprocessing import OrdinalEncoder,OneHotEncoder,QuantileTransformer
from sklearn.pipeline import FeatureUnion
import numpy as np
import pandas as pd


def prep_dat(df,ylabels=None):
    df = df.drop(columns = ['UNIQUE_ID'])
    
    i_one = df.loc[pd.isnull(df['GENDER'])].index
    i_two = df.loc[pd.isnull(df['ETHNICITY'])].index
    labels_update = list(np.append(i_one,i_two))
    print(labels_update)

    df = df.drop(labels=labels_update)
    
    df.reset_index(inplace=True,drop=True)
    #including only the values without missing gender and ethnicity
    df = df[pd.notnull(df['GENDER'])]
    df = df[pd.notnull(df['ETHNICITY'])]
    col_names = df.columns 
    df['HS_GPA'] = df['HS_GPA'].replace(0,np.nan)
    
    imputer_transformer = FeatureUnion(
    transformer_list = [
        ('features',SimpleImputer(strategy = 'constant',fill_value = 0)),
        ('indicators',MissingIndicator())])
    out_df = imputer_transformer.fit_transform(df)
    #imputed dfcreation
    col_names = np.append(col_names,['Ind_Mothers','Ind_Fathers','Ind_HS_GPA','Ind_SATRead','Ind_SATMath'])
    imputed_df = pd.DataFrame(out_df,columns = col_names)
    imputed_df[['Ind_Mothers','Ind_Fathers','Ind_HS_GPA','Ind_SATRead','Ind_SATMath']] = imputed_df[['Ind_Mothers','Ind_Fathers','Ind_HS_GPA','Ind_SATRead','Ind_SATMath']].astype(int)
    if np.any(ylabels):
        ylabels = ylabels.drop(labels=labels_update)
        ylabels.reset_index(inplace=True,drop=True)
        return imputed_df,ylabels
    else:
        return imputed_df

def transform_cat(prep_df,ylabels=None):
    #feature scaling and tranformations for categorical attributes
    col_names = prep_df.columns
    ordinal_att = ['COHORT','MothersEd','FathersEd'] 
    one_hot_att = ['NATIVE_COLLEGE','GENDER','ETHNICITY','RESIDENCY','AOA_RSNCODE','PARTNER_SCHOOL']
    num_att = ['HS_GPA','SATRead','SATMath']
    column_trans = ColumnTransformer([
      ('ordinal_cat',OrdinalEncoder(),ordinal_att),
      ('one_hot_cat',OneHotEncoder(),one_hot_att),
      ('num_att',QuantileTransformer(output_distribution='normal',random_state=22),num_att)],
        remainder = 'passthrough')
    trans_df = column_trans.fit_transform(prep_df)
    if np.any(ylabels):
        return trans_df,ylabels
    else:
        return trans_df        