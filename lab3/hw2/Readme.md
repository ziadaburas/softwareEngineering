# دليل فلاتر Django Template Language (DTL)

هذا الملف يحتوي على دليل شامل للفلاتر المدمجة في نظام قوالب Django، مصنفة حسب وظيفتها مع أمثلة عملية.

---

### النصوص والتنسيق

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `capfirst` | [span_0](start_span)يحول الحرف الأول من النص إلى حرف كبير[span_0](end_span). | `{{ "django"\|capfirst }}` |
| `lower` | [span_1](start_span)يحول كل أحرف النص إلى أحرف صغيرة[span_1](end_span). | `{{ "DJANGO"\|lower }}` |
| `upper` | [span_2](start_span)يحول كل أحرف النص إلى أحرف كبيرة[span_2](end_span). | `{{ "django"\|upper }}` |
| `title` | [span_3](start_span)يحول النص إلى تنسيق العنوان (بداية كل كلمة حرف كبير)[span_3](end_span). | `{{ "django template language"\|title }}` |
| `slugify` | [span_4](start_span)يحول النص إلى صيغة صديقة لمحركات البحث (URL-friendly)[span_4](end_span). | `{{ "Django Template Language"\|slugify }}` |
| `truncatechars` | [span_5](start_span)يختصر النص لعدد محدد من الأحرف ويضيف "..."[span_5](end_span). | `{{ "Django is a web framework"\|truncatechars:10 }}` |
| `truncatewords` | [span_6](start_span)يختصر النص لعدد محدد من الكلمات ويضيف "..."[span_6](end_span). | `{{ "Django is a powerful web framework"\|truncatewords:4 }}` |
| `wordwrap` | [span_7](start_span)يقسم النص إلى أسطر بعرض محدد من الأحرف[span_7](end_span). | `{{ "Django makes web development easy"\|wordwrap:10 }}` |
| `linebreaks` | [span_8](start_span)يحول فواصل الأسطر في النص إلى وسوم `<p>` و `<br>`[span_8](end_span). | `{{ my_text\|linebreaks }}` |

---

### الأرقام والحسابات

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `add` | [span_9](start_span)يضيف قيمة إلى المتغير (يعمل مع الأرقام والنصوص)[span_9](end_span). | `{{ 5\|add:"3" }}` |
| `floatformat` | [span_10](start_span)ينسق الأرقام العشرية لعدد محدد من المنازل[span_10](end_span). | `{{ 34.23234\|floatformat:2 }}` |
| `divisibleby` | [span_11](start_span)يتحقق إذا كان الرقم قابلاً للقسمة على قيمة معينة[span_11](end_span). | `{{ 21\|divisibleby:"3" }}` |
| `get_digit` | [span_12](start_span)يستخرج رقماً محدداً من عدد صحيح (بدءاً من اليمين)[span_12](end_span). | `{{ 123456\|get_digit:3 }}` |
| `filesizeformat` | [span_13](start_span)يحول قيمة عددية بالبايت إلى تنسيق مقروء (KB, MB, GB)[span_13](end_span). | `{{ 123456789\|filesizeformat }}` |

---

### القوائم والمصفوفات

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `first` | [span_14](start_span)يعرض العنصر الأول من القائمة[span_14](end_span). | `{{ my_list\|first }}` |
| `last` | [span_15](start_span)يعرض العنصر الأخير من القائمة[span_15](end_span). | `{{ my_list\|last }}` |
| `join` | [span_16](start_span)يدمج عناصر القائمة باستخدام فاصل محدد[span_16](end_span). | `{{ my_list\|join:", " }}` |
| `length` | [span_17](start_span)يعرض عدد العناصر في القائمة[span_17](end_span). | `{{ my_list\|length }}` |
| `slice` | [span_18](start_span)يعرض جزءاً (شريحة) من القائمة[span_18](end_span). | `{{ my_list\|slice:":2" }}` |
| `random` | [span_19](start_span)يعرض عنصراً عشوائياً من القائمة[span_19](end_span). | `{{ my_list\|random }}` |
| `dictsort` | [span_20](start_span)يرتب قائمة من القواميس تصاعدياً حسب مفتاح محدد[span_20](end_span). | `{{ users\|dictsort:"name" }}` |
| `dictsortreversed` | [span_21](start_span)يرتب قائمة من القواميس تنازلياً حسب مفتاح محدد[span_21](end_span). | `{{ users\|dictsortreversed:"age" }}` |
| `unordered_list` | [span_22](start_span)يحول قائمة متداخلة إلى قائمة HTML `<ul>` متداخلة[span_22](end_span). | `{{ nested_list\|unordered_list }}` |

---

### التواريخ والأوقات

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `date` | [span_23](start_span)ينسق التاريخ باستخدام رموز محددة[span_23](end_span). | `{{ my_date\|date:"Y-m-d" }}` |
| `time` | [span_24](start_span)ينسق الوقت باستخدام رموز محددة[span_24](end_span). | `{{ my_time\|time:"H:i:s" }}` |
| `timesince` | [span_25](start_span)يعرض الوقت المنقضي منذ تاريخ معين بصيغة مقروءة[span_25](end_span). | `{{ past_date\|timesince }}` |
| `timeuntil` | [span_26](start_span)يعرض الوقت المتبقي حتى تاريخ معين بصيغة مقروءة[span_26](end_span). | `{{ future_date\|timeuntil }}` |

---

### الأمان والترميز

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `escape` | [span_27](start_span)يهرب رموز HTML الخاصة لحماية التطبيق من هجمات XSS[span_27](end_span). | `{{ "<b>نص</b>"\|escape }}` |
| `safe` | [span_28](start_span)يمنع التهريب التلقائي للنص (يجب استخدامه بحذر)[span_28](end_span). | `{{ "<b>محتوى موثوق</b>"\|safe }}` |
| `force_escape` | [span_29](start_span)يقوم بالتهريب فوراً حتى لو كان النص معلم كآمن[span_29](end_span). | `{{ dangerous_var\|force_escape }}` |
| `striptags` | [span_30](start_span)يزيل كل وسوم HTML من النص[span_30](end_span). | `{{ "
نص مهم
"\|striptags }}` |
| `escapejs` | [span_31](start_span)يهرب الأحرف الخاصة في النص لاستخدامها بأمان في JavaScript[span_31](end_span). | `{{ "String with 'quotes'"\|escapejs }}` |
| `urlencode` | [span_32](start_span)يرمز النص لاستخدامه بأمان في عناوين URL[span_32](end_span). | `{{ "django/قوالب"\|urlencode }}` |

---

### فلاتر `humanize` (للتنسيق البشري)

**[span_33](start_span)ملاحظة:** لاستخدام هذه الفلاتر، يجب إضافة `django.contrib.humanize` إلى `INSTALLED_APPS` واستخدام `{% load humanize %}` في القالب[span_33](end_span).

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `intcomma` | [span_34](start_span)يضيف فاصلة (,) للآلاف في الأرقام الكبيرة[span_34](end_span). | `{{ 45000000\|intcomma }}` |
| `intword` | [span_35](start_span)يحول الأرقام الكبيرة إلى صيغة كلامية (مليون، مليار)[span_35](end_span). | `{{ 1200000000\|intword }}` |
| `apnumber` | [span_36](start_span)يحول الأرقام من 1 إلى 9 إلى كلمات باللغة الإنجليزية[span_36](end_span). | `{{ 1\|apnumber }}` |
| `naturalday` | [span_37](start_span)يعرض التاريخ بصيغة طبيعية (اليوم، أمس، غداً)[span_37](end_span). | `{{ my_date\|naturalday }}` |
| `naturaltime` | [span_38](start_span)يعرض الوقت بصيغة طبيعية (منذ دقيقتين، بعد ساعة)[span_38](end_span). | `{{ my_date\|naturaltime }}` |
| `ordinal` | [span_39](start_span)يحول العدد إلى صيغة ترتيبية بالإنجليزية (1st, 2nd, 3rd)[span_39](end_span). | `{{ 3\|ordinal }}` |

---

### فلاتر متنوعة

| الفلتر | الوصف | مثال |
| :--- | :--- | :--- |
| `default` | [span_40](start_span)[span_41](start_span)يعرض قيمة افتراضية إذا كان المتغير فارغاً أو غير موجود[span_40](end_span)[span_41](end_span). | `{{ my_variable\|default:"قيمة افتراضية" }}` |
| `default_if_none` | [span_42](start_span)يعرض قيمة افتراضية إذا كان المتغير `None` فقط[span_42](end_span). | `{{ my_variable\|default_if_none:"لا شيء" }}` |
| `yesno` | [span_43](start_span)يعرض قيمة مخصصة لـ `True`, `False`, أو `None`[span_43](end_span). | `{{ is_active\|yesno:"نعم,لا" }}` |
| `stringformat` | [span_44](start_span)ينسق سلسلة نصية وفقًا لصيغة محددة (مثل printf في C)[span_44](end_span). | `{{ order_id\|stringformat:"06d" }}` |

