import streamlit as st
import pandas as pd

#قراءة الملف 
file_path = 'C:/Users/manso/OneDrive/سطح المكتب/inventory system/KSA.xlsx'


# التحقق من وجود DataFrame في session_state
if 'df' not in st.session_state:
    try:
        df = pd.read_excel(file_path) 
        #نحول السيريال نمبر لنص صو احتجنا
        if 'Serial Number' in df.columns:
            df['Serial Number'] = df['Serial Number'].astype(str)
        st.session_state.df = df
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
        st.stop()  # ننهي التطبيق لو ماقدر يقرا الملف 
else:
    df = st.session_state.df  # استرجاع DataFrame من session_state

st.image("C:/Users/manso/OneDrive/سطح المكتب/inventory system/mbuzz-light-logo.png", width=400)


# العنوان
st.title(" Inventory Mangement System")
st.markdown('<p class="big-font"> FOR MBUZZ !</p>', unsafe_allow_html=True)



if 'show_stock' not in st.session_state:
    st.session_state.show_stock = False

#زر المخزون
if st.button("Toggle stock view / عرض أو إخفاء المخزون"):
    st.session_state.show_stock = not st.session_state.show_stock

# عرض المخزون إذا كانت الحالة True
if st.session_state.show_stock:
    st.write(df)


# خيار لتحديد العمود الذي ترغب في الفرز بناءً عليه
sort_column = st.selectbox("Select the sort column:", df.columns.tolist())

#  تحديد ترتيب الفرز 
sort_order = st.radio("Select sort order:", ('Ascending', 'Descending'))

#  تصفية البيانات حسب الفئة
category_filter = st.selectbox("Category / الفئة:", ['All'] + df['Category'].unique().tolist())

# تنفيذ التصفية
if category_filter != 'All':
    filtered_df = df[df['Category'] == category_filter]
else:
    filtered_df = df

# تنفيذ الفرز
if sort_order == 'Ascending':
    sorted_df = filtered_df.sort_values(by=sort_column)
else:
    sorted_df = filtered_df.sort_values(by=sort_column, ascending=False)

# عرض الداتا
st.dataframe(sorted_df)


# إدخال بيانات المنتج
category = st.selectbox("Category / الفئة:", ['Server', 'Parts', 'Switch', 'Cable', 'SSD', 'Accessories','Mother Board',
                                               ' Graphics Card', 'CPU','USB-Adapter', 'USB-Ethernet', 'USB','NIC', 'Transceiver', 'CPU-Cooler', 'PSU','Hard Drive Docking Station']
                                               , key='category_select')
Item = st.text_input("Item / العنصر:", key='Item_input')
item_description = st.text_input("Item Description / وصف العنصر:", key='item_description_input')
in_stock = st.number_input("In Stock / في المخزون:", min_value=0, key='in_stock_input')
serial_number = st.text_input("Serial Number / رقم السيريال:", key='serial_number_input')
location = st.text_input("Location / الموقع:", key='location_input')
asset_tag = st.text_input("Asset Tag / علامة الأصول:", key='asset_tag_input')
INV_Type = st.text_input("INV Type / نوع INV:", key='inv_type_input')
comments = st.text_input("Comments / تعليقات:", key='comments_input')

# إضافة منتج جديد
if st.button("Add product / إضافة منتج", key='add_product_button'):
    if all([Item, serial_number]):  #  لازم مايكونو فاضيين
        try:
            new_product = {
                'Category': category,
                'Item': Item,
                'Item Description': item_description,
                'In Stock': in_stock,
                'Serial Number': str(serial_number),
                'Location': location,
                'Asset Tag': asset_tag,
                'INV Type': INV_Type,
                'Comments': comments
            }
            # تحويل القاموس إلى DataFrame قبل دمجه
            new_product_df = pd.DataFrame([new_product])

            # دمج DataFrame
            df = pd.concat([df, new_product_df], ignore_index=True)  
            st.session_state.df = df  # تحديث DataFrame في session_state
            
            st.success("The product has been added successfully / تم إضافة المنتج بنجاح")
        except Exception as e:
            st.error(f"Error adding product: {e}")
    else:
        st.error("يرجى ملء جميع الحقول المطلوبة (العنصر ورقم السيريال).")




# حفظ التغييرات
if st.button("Save changes / حفظ التغييرات", key='save_changes_button'):
    try:
        df['Serial Number'] = df['Serial Number'].astype(str)
        df.to_excel(file_path, index=False)
        st.success("Changes saved in Excel file / تم حفظ التغييرات في ملف Excel!")
    except Exception as e:
        st.error(f"Error saving changes to Excel file: {e}")
import streamlit as st



# تنسيق النص
st.markdown(
    """
    <style>
    .big-font {
        font-size: 32px;
        color: #343636;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #C0C0C0 /* لون الخلفية */
    
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stButton>button {
        border: none;                /* إزالة الحدود */
        padding: 10px 20px;         /* padding */
        text-align: center;          /* محاذاة النص */
        text-decoration: none;       /* إزالة التسطير */
        display: inline-block;       /* عرض ككتلة مستقلة */
        font-size: 16px;             /* حجم الخط */
        margin: 4px 2px;            /* هوامش */
        cursor: pointer;             /* شكل المؤشر عند المرور */
        border-radius: 7px;         /* زوايا مستديرة */
    }
    
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .title {
        color: #C0C0C0;    /* لون الخط */
    }
    </style>
    """,
    unsafe_allow_html=True
)
