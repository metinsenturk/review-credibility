import pandas as pd
import matplotlib.pyplot as plt


def get_clean_users(con):

    query = """
    select * from
    users u
    inner join users_clean uc on u.user_id == uc.user_id
    left join user_spammers us on u.user_id == us.user_id
    left join user_positive_percentage upp on u.user_id == upp.user_id
    ;
    """

    return pd.read_sql_query(sql=query, con=con)


def get_clean_reviews(con):

    query = """
    select * from
    reviews r
    inner join reviews_clean rc on r.review_id == rc.review_id
    --left join reviews_meta rm on r.review_id == rm.review_id
    left join review_linguistics rl on r.review_id == rl.review_id
    ;
    """

    return pd.read_sql_query(sql=query, con=con)


def get_review_plots(df_g_rc):
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(15, 5))

    df_g_rc.sentiment_polarity.plot(ax=axes[0,0], title='sentiment_polarity')
    df_g_rc.sentiment_subjectivity.plot(ax=axes[0,1], title='sentiment_subjectivity')
    df_g_rc.ratio_content.plot(ax=axes[0,2], title='ratio_content')
    df_g_rc.ratio_lexical.plot(ax=axes[0,3], kind='box', title='ratio_lexical')
    df_g_rc.avg_len_sentences.plot(ax=axes[1,0], kind='kde', title='avg_len_sentences')
    df_g_rc.avg_len_words.plot(ax=axes[1,1], kind='kde', title='avg_len_words')
    df_g_rc.count_noun_phrases.plot(ax=axes[1,2], kind='hist', title='count_noun_phrases')
    df_g_rc.count_sentences.plot(ax=axes[1,3], kind='hist', title='count_sentences')

    fig.tight_layout()