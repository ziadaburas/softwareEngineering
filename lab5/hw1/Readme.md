## المحتوى الرئيسي

### 1. Django Form (النماذج اليدوية)
**الخصائص:**
- مرونة كاملة في التصميم
- تحكم دقيق في كل حقل
- إمكانية إنشاء نماذج معقدة

**المميزات:**
- مرونة عالية في التخصيص
- عدم الارتباط بنموذج قاعدة بيانات
- تحكم كامل في عملية التحقق

**العيوب:**
- يتطلب كتابة كود أكثر
- احتمالية أخطاء أعلى
- صيانة أصعب

### 2. Django ModelForm (النماذج المُولدة)
**الخصائص:**
- توليد تلقائي من نماذج Django
- ربط مباشر مع قاعدة البيانات
- تطبيق قواعد النموذج تلقائياً

**المميزات:**
- سرعة في التطوير
- أقل عرضة للأخطاء
- صيانة أسهل
- تزامن تلقائي مع النموذج

**العيوب:**
- مرونة أقل في التخصيص
- ارتباط وثيق بنموذج قاعدة البيانات
- صعوبة في النماذج المعقدة

## أمثلة الكود

### Django Form
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError('يجب أن يكون البريد من نطاق example.com')
        return email