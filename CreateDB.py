import psycopg2 as pg


class Create_Inm:

    @classmethod
    def create_table(cls):
        try:
            conn = pg.connect("host=127.0.0.1 port=5432 dbname=Inventory_Management_System user=postgres password=S123")
            cur = conn.cursor()
            create_table_inventory= '''CREATE TABLE IF NOT EXISTS inventory(
            inventory_id serial PRIMARY KEY,
            inventory_name VARCHAR(255) NOT NULL,
            quantity int not null,
            price int not null,
            type varchar(255) not null,
            weight numeric not null,
            dimensions varchar(255) not null,
            file_size float not null,
            download text not null,
            created_at TIMESTAMP DEFAULT now() NOT NULL
            '''
            cur.execiute(create_table_inventory)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(e)

