from rag_function import rag
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

encoded_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASEAAACuCAMAAABOUkuQAAABR1BMVEX///8kO5EgOJDv8fe6wNgAJ4o3S5kfN48cNY4AJonr7vb09frQ1Oawt9USL4z5+v3e4e4AIofIzuMOLYzCyN8rRJiiqs2TncZVZKUFKYn4//9KXKLj5vEAHoastNPO0uSDjr0AFYTk7/Zda6lTY6UAPpMAMY1serKLlsI0SJgARZXl+PoAlrq+5+0AiLnv+fwAEIPU5PB0f7UXZKUbWaBFV6DF2ekxe7FgmsKxz+Ohwd0AQ5V8iLmb2OZkxdk8ts4At8hRyNd20d3T7/Rxv9g2p8gAq8av2Oder84Ag7SL0eEQkr2o1eWPzN8AdbFHnMVmqc1tm8OctdV2l8FNjLrT9fhTk71XhrYAV54+c6xefbN9rs8oTpmdyN9+r9Q6aKcAAICMqM5hhLdTpMYAZa5pca0te7dobquZmsVhjbtNsM6s5OxxrNLtalj6AAAQJElEQVR4nO2b+3/SSL/Hk0DIhMvkMkAIdwqES0XkEqAtfTwrXalaWlqxFgHZ6naf9bT//89nZgIt2laPz5GuZ3feL1+ay2SY+TDzvQU5jsFgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGA9GdJMS/avH8TOy2dv919Onz5//F+GXX55d9qp/9ZB+IqqVvV8fvXr06/OnRJwlz15WmEiEan//1YtXv/7rZaV3vbuim73K7jPM5eZfOrafgdb+4xev9g96d1mezcru7m7/H72OqrOjw8f7X9Og1x8Mag83oJ+M6uzF4dFs4xuteoO9rQcZzo9CwfyQjqKz9uGw9b9w69XZcPZDPvFe4u4FQXKmrJw4d+iE1c8a+dw36N6brtRwIWbb2aKurLRSuZUT13Vfwa+PqjVqXN2/fXxc3K+rXNxI11ucMuusdxWlMyJFNuP4zMtr9ETDM3A/EUUN+kijwrJRgkxelWVxCSyl405H8YJkAiBJAMGYTlolSKsnYXpT1eiJHx8WSV+J2NeW2kbn99Mv9PFhVVLBWrzY3dQ9801bENtRIwETZP1sf9n4h+L1SLwDInPxlgR6AmI+LmjyvBAiCnmBsGgkBvCpKtBTLAX+V0Ieukx0gZxZGiJ3RNyXCkgjc6GQc0IUMiBpEfmKQrXH7T7+x+XlfIFiigtebCdtz3E0Kz4ZhhPaZTjT6EEBtqsxwFsVot7V1Y/Z2nfiFvF4BYmKQgVbaIFndqNQ0lwIxMOLa4VAwUiXyGytEl5FKiQawIJuUDUTAU61vl8hJR5XlGDxhAvmXntL80ouIcNa/bejOkKjGi9Ys6JZ3qxr7ZrIw3ZLEISdN1TSUWt9ChXweK0LG0skCOrNGuIF3nujUATPD3YjREfoXSpkuvHXHCEyoDTHZckBrBM5IX3c970KxWO5fkAU+v6MebZpZE6NzL6hHTbl91tHg5wE3m6LvHBQR2ecLX7EQwPjc8iDhhMybh+vbRGpeC68GQiTRYKMlTWEFdHRQiFVpLMLo8VeXChENlycXJNKXtWkshCTpOSIGmIy/p0KBRNor47KvTDC867Lp55pJWddGk+OXXEfL4C374BQ7udQO8qbgzCaSvNYKATbzrMbo7VZIiqN4KXfN8DW01lDVCWhKy0UKmIZJI+PzhJElgohopASo3L4A9T85Oi0i5AK/L0KhU04CYGzzQteamzmYEP+qNjmSbXSFxJ9sSzNpyHQrJRQxwusfhc0hTLfLIsfFw8fr8ud0QmCLMfZZAaW7qwhwdlq5BJRSCHGHKYXiwOqqwrRDchr/qSjEO3UQP+RQmkojQUw7nmaoFENCbzV57IQuvGj5ZnW5EN8E45bwJyoYr6SzY9xH20e7S0e3nq/JoVSZLRSrF636ZyLjkJmeGmNqEJBjRx4YrkS3X3GqkKukEBVcxNVhBINji4AtU3fq9DFDl8OgVFLfgHGXsALaMbpFkC6X2tMzAYvTRtoFITmQTAx7XnKI0mYdqDVXzy80VmTQmT/YIkgdPaVx0d3mRYMyCsKFehUBeC4fLwXV+xQmtoh2+d1RCNypGgz2X2XQti4c114syFXsRuAb4JOGEzg2I8/y5xgT8uj+Yk2MmAbr665PAwjqxLWxj3YnADQfg3zlcXDvjX5e19ouVYW1jnoImtIc3M5a6mQ4pX4zxupcSoHNFSdeEJshrAKXWrQhGQ8SDcssDlHIZAtEsK2E1CoStB5uHBrLKVDEGqgSSH/Do7dsNzWOorqC8DpO7nTtbAgRzkTO/vpm7o2qiXG2wDtY8f2ZvG0MlmPQm4a5wBRlmX6HcP0UiE/ulYoSTYZb8nXjYrOgsGrSnRWxgUenS9G9xkKASoQ9C/iIXyI0dJFuipBKCZRVyC6vxxLHByhaRvt2xCCdlhun2RGYTjxCs2mvP9v4QDu7Hmkftc8q3nkfXdipMOdfgQdXidua1KogHDQBQupVMqfg/gQlFQPEAQc7nFpUyCAEBcDpFHXTxqRQ7wQBEBvSuQvaBZItsV5L6iAdP6mnSIxpHANSisFkexSgbaB2Jh9iaoNtfGH/BCeHoujonaqZ9qvtXFdbDfRnj3ti+MtuNMrikIIlSt/ZoZ64rBWSoyuH5+tRSFvyIMppchxQKDHyVzJ4xHwF+y1S/SCrdJGTmZhOA8knXsOF+7l2JK2JSOIROQxaIYaumkUwp4wEOGRbJqmDEuF1K2xKMHMLHMUKb/VBvqT9sWTof+35pYsJ84GHjiDjQ2zo1uNN/FIPt8YcOeNgTre8x2PBtePr8fbKy6Kc+ylxz7yl5fM2efcdC1urD6wvEWPV/tLBYx6Ohl0GnOuL5vFg4FwOPxZOeCa9+flfvPgQ/u43Yu3P56c9pXJLKp39ivc1qDa6nOtnq9Scfk2+v2e16tsRrnPCyOuh6uj+b7dZB203lZ70Wo02gqqvqDblwykwmGjeJI0ultcuN495yLZSDZmezy2XQLW7Sxs48EUCpQi+kN91irLrKH4pL2dwBFieZwxkXwYE7FH80DthVcGeItCE9s2IMLKree3HqhcHbRFCYgR9WE+bYXtyeKgoHVOxPnWWeP9YQMIw5CAjv2QNz/6TdAeYj5JYDzZu/WGQ9leY/ljFX/WBBbs3mUn1opvtJxgzJwY8jgaxXbmHWocQB4e4yTGHARMSBOMMETDOzpoPVytWo8VHn4FcdvbiwOFhy+7WieZO+HiEH7UEVYoJ/Gob5jCLmmQhubgjg7ef6vg/38h7ncHgn5n2fi8Lu/Sb3FxPWwYSb/rpqmiug3DCPgda674VyDPe79AwQ5ywdftv3KdMniB8MkWh/XMkCvKO5WkVQbz0FSw3tThzjmpchcstHu7g9a68lYsSSAb0mRTE0t1klQGSAhTipA7/jqvIYRM2bOsQ3PuCJLxJVG0w2TGaiKhXVMyFG4l/lnEWYXFpVD9q6OoLZcQ54cClKxJVp5xPBpxRdAUQkIDlN/YQBC1A86XA/nbZprrrM2TqTmZBrokeZXTCpckgTROqUgFAy5SNgkBmny6CiTHECycX0liTiVVIuc+TTMkrctBIKwgQV0Fiysg9FXTtn29R9xmqMnzM1vsu7X8gKvzf5CcHjY28Rjz5QqOccHZ7RfRW8c/Wpglik2zL1DiSa1MK3JJJ1PHAml0+tBEREAR5wi+CK0AlboxWh8rqUuFctkITTUScf6zNFgAKYOkfU7qFvjaMLauHVEyMZ7BnS1eqOTQ4aaSK59KoD1HbZ8G2pV+Fed68PDWO7SNP9ZmhWgVn7e6Xn8JAgB511IhXXPmWE8WBZwoyJkgztNobh7nfBdUouxCIUHnFDcVIRiyAF1PzsICVpCW53L0S7j4yjA2bgLAYmK0pTVnsLkNse9ylZrHAA5j8ke/aFEXFoRwdEuh05MfL82CgJPaX8Q51Z/SdV1xFIpxWTpRK4nb4NgWk3IWCCL5lJeWTEw9ThWS8CUfKW1oKukiSKscKIyPUwFaktRtYVnBvoeVeLggd0608Qkaf0BnPS4ujk9gfuaR9wKmRV3YXc5++4/1xUJxHi5KEnXDTSzFQiGXcxlb7KA7qJN5+93L/Yepk7KGaTgKCUnVn8ZSyM4qcerWGo3Lu4g+QitmKHn/MGo3M7S1yZ/a23Ozgb8FT/ZcHgXkxhZx9kj4YIRrxNl/+Qq69fs6Ew6/7VhqCSDEp31Lhbx0k0EDL3NEqjtQzNKK/2Kv0MIkTKvXlVoiQdGZpo8qJJN3zi6y7JDB6dSAZe8fRetGofnZIG0Ni1ojb8oa+PSko2fwH9TDXgLJT/a4CwgvP3944/f1BotKoFDSEN1Tgpm9rZAHSs5GpG+ChJU1hIrOGuIhok3STty0ohDdwzCcCtLehfsDUWqog9mkK1xtva5h36/XaoNZf/CyN6sok0p8NNo8b8/n80afm+d3sLN359z2wnZVG+sLhZYoajjrGFhRDzgK0Zcb5Gv3FbJO9TTrpxvPXLFDgYUd6hoeKkrsS4XoO0YeaU7Je1GvvgtS/IoDCX34bQISno1CxmyFec9F2M5FIq1iAdvhcGErWmv1/PFqr0cKKe+kj47Pr/4xurfbH0EwlyXEOS+dl5kMLKwNddM8JC46KFOTpNCXq8DjXfgyifc5u0zyO28lec3/uULx6zfZFHD/TxlIOBSw9sT9/rvyKRiJh6F2GjXQThPy+Fw+jNYzSGvZmY650+MCYB4Ne8p1Lpk7X7tAnKphpwxQIe6ni0ZMLRVSSha1L8VAwHkzEeH8gC4mvu6hL53F5MLbS/rSdIc/V8hwYi1ixpxt5r9vGDO8YwKZk944EhpvW01h4mlk8wPYPsiM3rwGoN2SG5/EK0/5ymy84YxEeyuT35HPu4l273CNbszBkOm0NZmYa7l7EzHGQ3R+0DSd4n1O4QLUIAuOUJC8m5Zo3VlfxFX0Nw8LhbQgjkadN7TderdO+0DF+0axNSO/FxBr/56iUbQXK28Jjen0PHGazAyjkbIwep04SiZGoeZruV3lcF4bMz8a2mhuXl2N1l/zSJYgBBL2ZRCG8KTDCfyNIw++4S0ASN2cgG+BEpmdmqVtyYUYsTMqCRAB1En+QY4kkqz5bBF3gSNM/QnpygmDPCY+Nj33pa8b5NWyDpuxKRh1w6XmjDh7WN79U555pQY/mmt7G3vv4fyTfMopETTiQR8rNDX3Wg9RFHIFujk7ZOe6SRIPqckAxnlRk0rHQoLAl3LdcGoxN72YJW3TTu1e0SnEh/lp0EQvukkPyTjnJ10lnV+apWi3Adftj3c4qnGGbkC+CU5LeX58Irb5KTjFrr3vtjr825h5gLdh4u07bR/HH2AEy73q5UywDtYpzCo+n9d359fr86qq1/XZ96T4vrjwQ5gNFXtekPgGmuSaO29fW23QFt5ysXwlDXPSeGpVgrqROI3AGfZ5oTZq9N26G+7ckeT/Xdl4XAsnrMPEBPFyOzb1NE9RRxhXS9OKXZ6Cuaf8hp+OUcfO98lmHJujD1q+De9I8v++zI6qB4ONSc89Pt1z53f2iokZatQS81ZiuC1+sHfOtXYODEPTHpc0G+/k05Y1HZuH/6TfmleP9hcH0ShXq0Q3DnqzycanoX42SKHTYkKz9uDOFeJz3XfmyNDeucXG3Lyd5P+d6b3av2O+UW6zytV6yvbpIPpptN2c5stniY4/AZHZsM2rhx/mX0nv1X9/Y9NguTZ7ldqswgUaj4+P5vk1/878p6P36NE3fVPt/ahDM9YoF62++SeZIcrm00dPe1+5vzHrtEfb98ZU/wh2nz//5fLulVHbujodvV/jj6b/n1B9Sf6H5uVn+yda7fVnk+HV5KHezP/kVC+f0f/H+uzlJaZyebm7O9jbm23VmDw3VHuXL59RXu7uXlYqtQ2mzl1Eo9UqCR8ZDAaDwWAwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMBgMBoPBYDAYDAaDwWAwGAwGg8FgMB6K/wG42RDD0tDVZQAAAABJRU5ErkJggg=="


image_data = base64.b64decode(encoded_image.split(",")[1])
image = Image.open(BytesIO(image_data))


st.sidebar.image(image, use_column_width=True)


st.markdown(
    """
    <h1 style='color: 	#1E90FF;'>Anadolu Sigortanın Yeni Sigorta Evreni anadoLia'ya Hoşgeldiniz</h1>
    """,
    unsafe_allow_html=True
)


# set initial message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant","content": "Ben anadoLia, sana nasıl yardımcı olabirim ?",  "color":"#0000FF"}
    ]


if "messages" in st.session_state.keys():
    # display messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# get user input
user_prompt = st.chat_input()
expander = ("Atatürk'ün talimatıyla kurulmuştur."
            "Türkiye'nin ilk ulusal sigorta şirketidir."
            "Sigortacılık birikiminin getirdiği güçlü bir kurumsal yapıya sahiptir."
            "Ürün yaratmada öncüdür.Teknolojide öncüdür."
            "Kendini yenileme kabiliyetiyle öncülüğünün devamlılığını sağlar."
            "Toplumsal sorumlulukta öncü role sahiptir.Etik değerlere sahiptir."
            "Verdiği sözleri mutlaka tutar.Şeffaflık ilkesine sahiptir./n"
            "İnsani değerlerden vazgeçmez.Sürekliliği olan bir mali güce sahiptir."
            "Yaygın ve etkin hizmet ağına sahiptir."
            "Gelişmiş, nitelikli insan kaynağına sahiptir."
            "İş Bankası sinerjisinden güç alır.")
with st.sidebar:
    with st.expander('Anadolu Sigorta', expanded=True):
        st.write(expander)



if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = rag(user_prompt)
            st.markdown(
                f"<div style='color: #1E90FF;'>{ai_response}</div>",
                unsafe_allow_html=True
            )

    new_ai_message = {"role": "user", "content": ai_response}
    st.session_state.messages.append(new_ai_message)

