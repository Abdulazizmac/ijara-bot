import aiosqlite

async def create_db():
    async with aiosqlite.connect("ijara.db") as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS ijara_ber(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tur VARCHAR(50),
            xona VARCHAR(50),
            tuman VARCHAR(50),
            kvadrat VARCHAR(50),
            jihoz1 VARCHAR(50),
            jihoz2 VARCHAR(50),
            jihoz3 VARCHAR(50),
            muddat VARCHAR(50),
            narx VARCHAR(50),
            phone VARCHAR(50),
            photo VARCHAR(50)
        )
        """)
        await conn.commit()

async def save_to_db(data, phone):
    async with aiosqlite.connect("ijara.db") as conn:
        await conn.execute("""
        INSERT INTO ijara_ber(tur, xona, tuman, kvadrat, jihoz1, jihoz2, jihoz3, muddat, narx, phone, photo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("tur"),
            data.get("xona"),
            data.get("tuman"),
            data.get("kvadrat"),
            data.get("jihoz1"),
            data.get("jihoz2"),
            data.get("jihoz3"),
            data.get("muddat"),
            data.get("narx"),   
            phone,
            data.get("photo")
        ))
        await conn.commit()