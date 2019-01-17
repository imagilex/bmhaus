# Generated by Django 2.0.7 on 2019-01-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_pieza_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='banco',
            field=models.CharField(choices=[('BANAMEX', 'BANAMEX'), ('BANCOMEXT', 'BANCOMEXT'), ('BANOBRAS', 'BANOBRAS'), ('BBVA BANCOMER', 'BBVA BANCOMER'), ('SANTANDER', 'SANTANDER'), ('BANJERCITO', 'BANJERCITO'), ('HSBC', 'HSBC'), ('GE MONEY', 'GE MONEY'), ('BAJÍO', 'BAJÍO'), ('IXE', 'IXE'), ('C.B. INBURSA', 'C.B. INBURSA'), ('INTERACCIONES', 'INTERACCIONES'), ('MIFEL', 'MIFEL'), ('SCOTIABANK', 'SCOTIABANK'), ('BANREGIO', 'BANREGIO'), ('INVEX', 'INVEX'), ('BANSI', 'BANSI'), ('AFIRME', 'AFIRME'), ('BANORTE', 'BANORTE'), ('ABNAMRO', 'ABNAMRO'), ('AMERICAN EXPRESS', 'AMERICAN EXPRESS'), ('BAMSA', 'BAMSA'), ('TOKYO', 'TOKYO'), ('JP MORGAN', 'JP MORGAN'), ('BMONEX', 'BMONEX'), ('VE POR MAS', 'VE POR MAS'), ('ING', 'ING'), ('DEUTSCHE', 'DEUTSCHE'), ('CREDIT SUISSE', 'CREDIT SUISSE'), ('AZTECA', 'AZTECA'), ('AUTOFIN', 'AUTOFIN'), ('BARCLAYS', 'BARCLAYS'), ('COMPARTAMOS', 'COMPARTAMOS'), ('FAMSA', 'FAMSA'), ('BMULTIVA', 'BMULTIVA'), ('PRUDENTIAL', 'PRUDENTIAL'), ('WAL-MART', 'WAL-MART'), ('NAFIN', 'NAFIN'), ('REGIONAL', 'REGIONAL'), ('BANCOPPEL', 'BANCOPPEL'), ('ABC CAPITAL', 'ABC CAPITAL'), ('UBS BANK', 'UBS BANK'), ('FÁCIL', 'FÁCIL'), ('VOLKSWAGEN', 'VOLKSWAGEN'), ('CIBanco', 'CIBanco'), ('BBASE', 'BBASE'), ('BANKAOOL', 'BANKAOOL'), ('PagaTodo', 'PagaTodo'), ('BIM', 'BIM'), ('SABADELL', 'SABADELL'), ('BANSEFI', 'BANSEFI'), ('HIPOTECARIA FEDERAL', 'HIPOTECARIA FEDERAL'), ('MONEXCB', 'MONEXCB'), ('GBM', 'GBM'), ('MASARI CB', 'MASARI CB'), ('C.B. INBURSA', 'C.B. INBURSA'), ('VALUÉ', 'VALUÉ'), ('CB BASE', 'CB BASE'), ('TIBER', 'TIBER'), ('VECTOR', 'VECTOR'), ('B&B', 'B&B'), ('C.B. INTERCAM', 'C.B. INTERCAM'), ('MULTIVA', 'MULTIVA'), ('ACCIVAL', 'ACCIVAL'), ('MERRILL LYNCH', 'MERRILL LYNCH'), ('FINAMEX', 'FINAMEX'), ('VALMEX', 'VALMEX'), ('ÚNICA', 'ÚNICA'), ('ASEGURADORA MAPFRE', 'ASEGURADORA MAPFRE'), ('AFORE PROFUTURO', 'AFORE PROFUTURO'), ('CB ACTINBER', 'CB ACTINBER'), ('ACTINVE SI', 'ACTINVE SI'), ('SKANDIA', 'SKANDIA'), ('CONSULTORÍA', 'CONSULTORÍA'), ('CBDEUTSCHE', 'CBDEUTSCHE'), ('ZURICH', 'ZURICH'), ('ZURICHVI', 'ZURICHVI'), ('HIPOTECARIA SU CASITA', 'HIPOTECARIA SU CASITA'), ('C.B. INTERCAM', 'C.B. INTERCAM'), ('C.B. VANGUARDIA', 'C.B. VANGUARDIA'), ('BULLTICK C.B.', 'BULLTICK C.B.'), ('STERLING', 'STERLING'), ('FINCOMUN', 'FINCOMUN'), ('HDI SEGUROS', 'HDI SEGUROS'), ('ORDER', 'ORDER'), ('AKALA', 'AKALA'), ('JP MORGAN C.B.', 'JP MORGAN C.B.'), ('REFORMA', 'REFORMA'), ('STP', 'STP'), ('TELECOMM', 'TELECOMM'), ('EVERCORE', 'EVERCORE'), ('SKANDIA', 'SKANDIA'), ('SEGMTY', 'SEGMTY'), ('ASEA', 'ASEA'), ('KUSPIT', 'KUSPIT'), ('SOFIEXPRESS', 'SOFIEXPRESS'), ('UNAGRA', 'UNAGRA'), ('OPCIONES EMPRESARIALES DEL NOROESTE', 'OPCIONES EMPRESARIALES DEL NOROESTE'), ('LIBERTAD', 'LIBERTAD'), ('CLS', 'CLS'), ('INDEVAL', 'INDEVAL'), ('N/A', 'N/A')], default='BANAMEX', max_length=100),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='clabe',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono_2',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono_3',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='extension',
            field=models.CharField(blank=True, default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=10),
            preserve_default=False,
        ),
    ]
