import streamlit as st
from sqlalchemy import text

list_class = ['', 'Economy', 'VIP', 'VVIP', 'Reguler',]
list_gender = ['', 'male', 'female']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://radityacr740:o8KrhDcWj4wN@ep-super-smoke-81752083.us-east-2.aws.neon.tech/fpmbddb")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS TICKETS (id serial, class_name varchar, supporter_name varchar, gender char(25), \
                                                       stadium_name varchar, ticket_price varchar, match_name text, time_info time, date_info date);')
    session.execute(query)

st.header('FOOTBALL TICKETS')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM tickets ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO tickets (class_name, supporter_name, gender, stadium_name, ticket_price, match_name, time_info, date_info) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':None, '8':None})
            session.commit()

    data = conn.query('SELECT * FROM tickets ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        class_name_lama = result["class_name"]
        supporter_name_lama = result["supporter_name"]
        gender_lama = result["gender"]
        stadium_name_lama = result["stadium_name"]
        ticket_price_lama = result["ticket_price"]
        match_name_lama = result["match_name"]
        time_info_lama = result["time_info"]
        date_info_lama = result["date_info"]

        with st.expander(f'a.n. {supporter_name_lama}'):
            with st.form(f'data-{id}'):
                class_name_baru = st.selectbox("class_name", list_class, list_class.index(class_name_lama))
                supporter_name_baru = st.text_input("supporter_name", supporter_name_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama))
                stadium_name_baru = st.text_input("stadium_name", stadium_name_lama)
                ticket_price_baru = st.text_input("ticket_price", ticket_price_lama)
                match_name_baru = st.text_input("match_name", match_name_lama)
                time_info_baru = st.time_input("time_info", time_info_lama)
                date_info_baru = st.date_input("date_info", date_info_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE tickets \
                                          SET class_name=:1, supporter_name=:2, gender=:3, stadium_name=:4, \
                                          ticket_price=:5, match_name=:6, time_info=:7, date_info=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':class_name_baru, '2':supporter_name_baru, '3':gender_baru, '4':str(stadium_name), 
                                                    '5':ticket_price_baru, '6':match_name_baru, '7':time_info_baru, '8':date_info_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM tickets WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
