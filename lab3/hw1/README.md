# مقارنة شاملة بين محركات قوالب Django

هذا الملف يقدم مقارنة مفصلة بين أربعة من أشهر محركات القوالب المستخدمة في إطار عمل Django، وهي:
* **Django Template Language (DTL)**
* **Jinja2**
* **Mako**
* **Chameleon**

الهدف هو توضيح الفروقات الرئيسية لمساعدة المطورين على اختيار الأداة الأنسب لمشاريعهم.

***

## مقارنة الميزات التقنية

| الميزة | Django DTL | Jinja2 | Mako | Chameleon |
| :--- | :---: | :---: | :---: | :---: |
| **التكامل الأصلي مع Django** | ✔ | 🗙 | 🗙 | 🗙 |
| **سهولة الاستخدام والتعلم** | ✔ | ✔ | ✔ | 🗙 |
| **التخزين المؤقت المدمج** | ✔ | ✔ | ✔ | 🗙 |
| **التعبيرات البرمجية الكاملة** | 🗙 | 🗙 | ✔ | 🗙 |
| **الكود البايثوني المضمن** | 🗙 | 🗙 | ✔ | 🗙 |
| **الأمان (sandbox)** | ✔ | ✔ | ✔ | ✔ |
| **دعم الوراثة في القوالب** | ✔ | ✔ | ✔ | ✔ |
| **دعم التدويل (i18n)** | ✔ | ✔ | 🗙 | ✔ |

*[span_0](start_span)جدول مستخلص من المصدر.[span_0](end_span)*

***

## مقارنة الأداء

| معيار المقارنة | Django DTL | Jinja2 | Mako | Chameleon |
| :--- | :--- | :--- | :--- | :--- |
| **سرعة التنفيذ (غير مخبأ)** | [span_1](start_span)بطيء نسبياً[span_1](end_span) | [span_2](start_span)أسرع بـ 4.5 مرة من DTL[span_2](end_span) | [span_3](start_span)أسرع بـ 5 مرات من DTL[span_3](end_span) | [span_4](start_span)سريع جداً[span_4](end_span) |
| **سرعة التنفيذ (مخبأ)** | [span_5](start_span)متوسط[span_5](end_span) | [span_6](start_span)أسرع بـ 10 مرات من DTL[span_6](end_span) | [span_7](start_span)أسرع بـ 12 مرة من DTL[span_7](end_span) | [span_8](start_span)أسرع بـ 9 مرات من DTL[span_8](end_span) |
| **استهلاك الذاكرة** | [span_9](start_span)مرتفع[span_9](end_span) | [span_10](start_span)أقل بـ 6MB من DTL[span_10](end_span) | [span_11](start_span)منخفض جداً[span_11](end_span) | [span_12](start_span)منخفض[span_12](end_span) |
| **أداء الحلقات التكرارية** | [span_13](start_span)جيد في القوائم الصغيرة[span_13](end_span) | [span_14](start_span)ممتاز في القوائم الكبيرة[span_14](end_span) | [span_15](start_span)ممتاز[span_15](end_span) | [span_16](start_span)جيد جداً[span_16](end_span) |

***

## مقارنة بنية الكود

| ميزة الكود | DTL | Jinja2 | Mako | Chameleon |
| :--- | :--- | :--- | :--- | :--- |
| **الحلقات التكرارية** | [span_17](start_span)`{% for %}` مع `empty`[span_17](end_span) | [span_18](start_span)`{% for %}` مع `{% else %}`[span_18](end_span) | [span_19](start_span)`% for` مع `endfor %`[span_19](end_span) | [span_20](start_span)`tal:repeat`[span_20](end_span) |
| **الشروط** | [span_21](start_span)`{% if %}`... `{% endif %}`[span_21](end_span) | [span_22](start_span)`{% if %}`... `{% endif %}`[span_22](end_span) | [span_23](start_span)`%if`... `% endif`[span_23](end_span) | [span_24](start_span)`tal.condition`[span_24](end_span) |
| **السمات الشرطية** | [span_25](start_span)داخل بلوك `{% %}`[span_25](end_span) | [span_26](start_span)تعبير ثلاثي داخل `{{ }}`[span_26](end_span) | [span_27](start_span)تعبير شرطي مباشر[span_27](end_span) | [span_28](start_span)`tal attributes`[span_28](end_span) |
| **تنسيق القيم** | [span_29](start_span)فلتر `floatformat`[span_29](end_span) | [span_30](start_span)دالة `format()`[span_30](end_span) | [span_31](start_span)`%`[span_31](end_span) | [span_32](start_span)دالة `format` داخل `python:`[span_32](end_span) |

***

### خلاصة التوصيات

* **[span_33](start_span)DTL**: مثالي للمبتدئين والمشاريع التي تعطي الأولوية للتكامل السلس مع Django.[span_33](end_span)
* **[span_34](start_span)Jinja2**: يقدم توازنًا ممتازًا بين الأداء وسهولة الاستخدام، وهو مناسب للمشاريع التي تحتاج سرعة أعلى.[span_34](end_span)
* **[span_35](start_span)Mako**: الخيار الأفضل للأداء الأقصى والمشاريع التي تتطلب قوة برمجية عالية في القوالب.[span_35](end_span)
* **[span_36](start_span)Chameleon**: موجه لمشاريع XML/HTML المعقدة والتطبيقات التي تحتاج نظام قوالب قائم على السمات.[span_36](end_span)
