# -*- coding: utf-8 -*-
"""
نظام المبيعات والمرتجعات — محل الكمبيوتر
بدون سعر تكلفة + شريط إحصائيات علوي دائم
التشغيل: python main.py

★ محصّن ضد الانهيار الصامت:
  - قاعدة البيانات تُفتح دائماً بجانب البرنامج (وليس مجلد التشغيل)،
    وإن كان الموقع محمياً للقراءة فقط يتراجع تلقائياً لمجلد آمن.
  - ملف shop.db قديم/تالف → يُحفظ جانباً ويبدأ البرنامج بقاعدة جديدة.
  - أي خطأ يظهر في صندوق عربي واضح ويسجل في error_log.txt.

★★★ الإصدار 2 — إضافات فقط دون المساس بأي شيء يعمل:
  1) تسجيل دخول بكلمة مرور (بائع/مدير) محفوظة مشفرة (hash)
  2) سجل تدقيق (Audit Log) يسجل كل الإجراءات تلقائياً
  3) تصدير Excel حقيقي (xlsx) بمكتبات قياسية فقط (zipfile)
  4) تصفية الأرشيف بمدى تاريخ بصيغ متعددة + إجمالي تراكمي
  5) اسم العميل الاختياري (عمود customer_name بترقية آمنة)
  6) فاتورة متعددة الأصناف (سلة) تُحفظ دفعة واحدة
     ✅ زر «حفظ الفاتورة كاملة» موجود بكل سلوكه: تأكيد بالعدد والإجمالي،
     حفظ دفعة واحدة، تفريغ السلة، تحديث الشريط العلوي، تسجيل في سجل
     التدقيق، سؤال التصدير إلى Excel، ومنع الحفظ عند سلة فارغة أو يوم مغلق

★★★ الإصدار 3 — نظام المستخدمين (إضافات فقط دون المساس بأي شيء يعمل):
  1) جدول users: حساب خاص لكل بائع + ترقية تلقائية لكلمة مرور المدير القديمة
  2) دخول باسم مستخدم وكلمة مرور (وإنشاء حساب المدير عند أول تشغيل)
  3) كل عملية تُسجّل باسم البائع (عمود seller_name بترقية آمنة) وتظهر في
     الجداول ونتائج البحث وتصدير CSV و Excel
  4) البائع يرى عملياته فقط — والمدير يرى الكل مع قائمة فلترة حسب البائع
  5) شاشة إدارة المستخدمين (إضافة/إيقاف/تفعيل/إعادة تعيين كلمة مرور) للمدير
  6) شاشة تقرير أداء البائعين بمدى تاريخ + إجمالي تراكمي + تصدير Excel
  7) اسم المستخدم ودوره تحت الشعار + تغيير كلمة المرور لأي مستخدم

★★★ الإصدار 4 — إضافات فقط دون المساس بأي شيء يعمل:
  1) زر «🔄 تبديل المستخدم» دون إغلاق البرنامج: تصفير الجلسة وتكييف
     الشريط الجانبي والشاشات مع صلاحيات المستخدم الجديد
  2) شاشة «📊 لوحة المعلومات» للمدير: فترات سريعة + 6 بطاقات + أفضل 5 أصناف
  3) رسم بياني بالأعمدة لصافي آخر 30 يوم عمل (tk.Canvas فقط) داخل اللوحة:
     أخضر للموجب، أحمر للسالب، وبرتقالي لليوم الجاري غير المغلق
  4) فلتر النوع (الكل/بيع/مرتجع) في «عمليات اليوم» يتكامل مع فلتر البائع
  5) تلميحات Tooltip عربية على كل الأزرار تظهر بعد 600 مللي ثانية

★★★ الإصدار 5 — نظام الأنواع الثلاثة (نقداً / شبكة / مرتجع):
تحديث منطق النوع فقط — كل مقارنات النوع «بيع» القديمة استُبدلت
بمقارنات النوعين الجديدين «نقداً» و«شبكة»، ولا شيء آخر تغيّر:
  1) ترقية آمنة بلا فقد بيانات: عمليات «بيع» القديمة تصبح «نقداً»،
     وعمودا total_cash و total_network يُضافان إلى daily_reports
     (التقارير القديمة: total_cash = total_sales و total_network = 0)
  2) day_totals ترجع (عدد العمليات، نقداً، شبكة، المرتجعات، الإجمالي)
     والإجمالي = نقداً + شبكة − المرتجعات
  3) الشريط العلوي 5 بطاقات: العدد / نقداً (أخضر) / شبكة (أزرق) /
     المرتجعات (أحمر) / الإجمالي (أزرق)
  4) إغلاق اليوم: ملخص يفصل الدرج النقدي عن كشف جهاز الشبكة قبل القفل،
     وحفظ total_cash و total_network مع total_sales = نقداً + شبكة
  5) الأرشيف وتفاصيل اليوم وتصديراته: نقداً وشبكة منفصلين في كل مكان
  6) فلتر عمليات اليوم: (الكل / نقداً / شبكة / مرتجع) مع فلتر البائع
  7) تقرير أداء البائعين: البائع | عدد العمليات | نقداً | شبكة |
     المرتجعات | الصافي — وصف الإجمالي التراكمي بنفس الأعمدة
  8) لوحة المعلومات: «إجمالي المبيعات» يبقى نقداً + شبكة مجتمعين،
     مع بطاقتين صغيرتين «مبيعات نقداً» و«مبيعات شبكة» للفترة المختارة

★★★ الإصدار 6 — نظام الطباعة الحرارية (Epson TM-T20III — ورق 80mm):
إضافات فقط دون المساس بأي شيء يعمل — تقارير اليوم فقط، بلا فواتير عملاء:
  1) وحدة طباعة مستقلة: EnumPrinters لجلب طابعات ويندوز، رسم عربي متصل
     سليم بعرض 576 بكسل (arabic_reshaper + get_display + خط arial/tahoma)،
     وتحويل الصورة لأوامر ESC/POS نقطية خام (GS v 0) تُرسل عبر winspool.drv
     (OpenPrinter / StartDocPrinter / WritePrinter / EndDocPrinter) بلا نوافذ
     طباعة، ثم أمر قص الورق (GS V) بعد كل طباعة
  2) المكتبات المطلوبة: pillow + arabic_reshaper + python-bidi بأمر واحد:
     pip install pillow arabic-reshaper python-bidi — والبرنامج يعمل كاملاً
     بدونها (تُفحص عند بدء التشغيل): أزرار الطباعة تعرض رسالة التثبيت فقط
     ولا ينهار أي شيء أبداً
  3) شاشة «⚙️ إعدادات الطباعة» للمدير (زر جديد في الشريط الجانبي): قائمة
     الطابعات + تحديث القائمة + طباعة تجريبية + اسم المحل + خيار الطباعة
     التلقائية عند الإغلاق — كلها تُحفظ في جدول settings الموجود
  4) تقرير إغلاق اليوم المطبوع بالتنسيق الحراري القياسي: اسم المحل ثم =====
     ثم التاريخ واسم اليوم ووقت الإغلاق، الإحصائيات سطراً لكل واحدة، ثم
     الإجمالي بخط أكبر، وأسفلها «أغلق بواسطة» وسطر الشكر
  5) ربط الطباعة بالإغلاق: طباعة تلقائية إن فُعّل الخيار أو بسؤال «هل تريد
     طباعة تقرير اليوم؟» بعد سؤال العرض وليس بدله — وفشل الطباعة لا يلغي
     حفظ اليوم أبداً (الحفظ حدث قبلها)
  6) إعادة طباعة أي يوم من الأرشيف: زر في نافذة تفاصيل اليوم + زر في شريط
     الأرشيف، من بيانات daily_reports المحفوظة، مع سطر «إعادة طباعة»
     والوقت الحالي وتسجيل في سجل التدقيق باسم من طبع

★★★ الإصدار 7 — حماية البيانات بخمس طبقات + الطباعة المحسّنة بمعاينة وA4:
إضافات فقط دون المساس بأي شيء يعمل:
  1) نسخة يومية تلقائية بعد كل «إغلاق يوم» ناجح مباشرة: backups/daily/
     backup_YYYY-MM-DD.db — يُحتفظ بآخر 30 نسخة فقط (حذف الأقدم تلقائياً)
     وفشل النسخ لا يلغي إغلاق اليوم أبداً (رسالة تحذير + error_log فقط)
  2) نسخة شهرية دائمة أول إغلاق في الشهر: backups/monthly/monthly_YYYY-MM.db
     — لا تُحذف أبداً
  3) مجلد نسخ خارجي ثانوي: زر اختياره في شاشة النسخ (يُحفظ في settings
     بمفتاح external_backup_dir) وكل نسخة يومية وشهرية تُنسخ في المكانين
     معاً، وإن فشل الخارجي تستمر الداخلية مع تحذير + زر فتح مجلد النسخ
  4) شاشة «🗄️ النسخ والاستعادة» للمدير (زر جديد في الشريط الجانبي): جدول
     بكل النسخ (النوع/الاسم/التاريخ/المكان/الحجم/عدد العمليات داخل النسخة
     بفتحها قراءة فقط عبر sqlite3 دون المساس بالقاعدة الحالية) + نسخة
     فورية الآن (آخر 10) + استعادة آمنة (فحص صحة النسخة ثم تحذير قوي ثم
     نسخة أمان pre_restore_... ثم استبدال الملف ثم رسالة إعادة التشغيل)
  5) تصدير الطوارئ الشامل: ملف xlsx متعدد الأوراق (العمليات/التقارير
     اليومية/المستخدمون/سجل التدقيق) بنفس منطق zip الموجود دون مكتبات
     خارجية إضافية
  6) حل جذري لمشكلة الصفحات البيضاء على طابعات A4: التقارير تُنشأ ملفات
     PDF قياسية عبر reportlab (pip install reportlab) بخط tahoma/arial
     مسجل ونفس التشكيل العربي الموجود — وغياب reportlab لا ينهي البرنامج
  7) نافذة «👁️ معاينة قبل الطباعة» (900×700) قبل أي طباعة A4: تعرض
     المحتوى كما سيُطبع تماماً + زر «طباعة A4 (PDF)» يفتح حوار الطباعة
     القياسي في ويندوز (تختار طابعة A4 منه فتختفي الصفحات البيضاء) + زر
     «طباعة حرارية 80mm» بنظام ESC/POS الموجود + زر إلغاء
  8) أزرار جديدة: «🖨 طباعة/معاينة A4» في نافذة تفاصيل اليوم وفي شريط
     الأرشيف + «📄 تقرير الفترة A4» بعد فلترة مدى التاريخ بعنوان
     «تقرير فترة من [تاريخ] إلى [تاريخ]» مع جدول الأيام والإجمالي التراكمي
  9) تلميحات للأزرار الجديدة + كل طباعة A4 تُسجل في سجل التدقيق
     («طباعة A4 — [نوع التقرير]») + سطر توضيحي في إعدادات الطباعة بأن
     تقارير A4 تُطبع عبر المعاينة وPDF ولا تحتاج اختيار طابعة مسبقاً

★★★ الإصدار 8 — سبعة تحسينات تفاعلية (إضافات فقط دون المساس بأي شيء يعمل):
  1) سجل تدقيق تفاعلي: النقر على صف يفلتر حسب المستخدم، والنقر على عمود
     «الإجراء» يفلتر بهذا الإجراء (كل من حفظ فاتورة مثلاً) + زر «عرض الكل»
     يلغي الفلتر + سطر ملون فوق الجدول يوضح الفلتر النشط وعدد السجلات +
     قائمة منسدلة «الإجراء» تختصر الفلترة الشائعة — الفلترة عرضية في
     الذاكرة فقط ولا تمس قاعدة البيانات
  2) تسجيل الدخول بقائمة منسدلة: حقل اسم المستخدم أصبح Combobox بكل
     المستخدمين المفعّلين (المدير أولاً ثم الباقي أبجدياً) — رسائل الخطأ
     الثلاث ومحاولات الدخول الفاشلة في سجل التدقيق تبقى كما هي تماماً
  3) تبديل المستخدم يغلق كل النوافذ المفتوحة فوراً (تتبع مركزي لكل نافذة
     Toplevel تُفتح) مع إفراغ السلة (تحذير السلة الحالي باقٍ كما هو) —
     وتدقيق «تبديل مستخدم — إغلاق [عدد] نافذة مفتوحة»
  4) دمج أزرار شريط الأرشيف وأزرار نافذة تفاصيل اليوم في زر «⚙️ الإجراءات»
     واحد يفتح قائمة منسدلة بكل الخيارات — نفس الدوال ونفس المنطق تماماً
  5) نظام صلاحيات دقيق يمنحها المدير: عمود permissions بترقية آمنة بلا
     فقد بيانات + عشر صلاحيات بمربعات اختيار عند إضافة/تعديل المستخدم +
     دالة has_permission تحل محل فحوصات «المدير فقط» (الاستبدال المصرح به
     بهذه الجلسة) + كل منح/سحب يُسجل في سجل التدقيق (من أعطى/سحب ماذا ومن)
  6) تنظيم الشريط الجانبي في مجموعات بعناوين فاصلة صغيرة (العمليات /
     التقارير / الإدارة) تظهر فقط إن كان في المجموعة زر ظاهر حسب
     الصلاحيات — نفس الأزرار ونفس دوالها، تنظيم بصري فقط
  7) قائمة المستخدم: زر واحد أسفل الشريط «👤 [الاسم] ([الدور])» يفتح قائمة
     منسدلة تجمع: تغيير كلمة المرور / نسخة احتياطية الآن / تبديل المستخدم /
     خروج — نفس الدوال الأربع الموجودة دون أي تغيير فيها

★★★ الإصدار 9 — نافذة تسجيل الدخول المحسّنة (8 ميزات بصرية وتفاعلية):
تحسين لنافذة الدخول فقط دون أي مساس بشاشات البرنامج الأخرى — والتعديل
المصرح به الوحيد: إعادة بناء كود بناء نافذة الدخول الحالية (login_flow
ودوالها الداخلية + login_dialog بنفس المنطق حرفياً: نفس رسائل الخطأ
الثلاثة، نفس تسجيل audit_log للمحاولات الفاشلة، نفس شرط active=1،
نفس شاشة إنشاء حساب المدير أول مرة) مع الشكل والميزات الجديدة فقط:
  1) زر عين 👁 داخل حقل كلمة المرور (يسار الحقل) في نافذة الدخول وشاشة
     إنشاء المدير ونافذة تغيير كلمة المرور: 👁 عند الإخفاء و🙈 عند
     الإظهار، ويعود للإخفاء تلقائياً بعد 5 ثوانٍ
  2) زر الدخول عريض بعرض البطاقة بلون ACCENT: يفتح درجة أفتح عند مرور
     المؤشر، ويغمق لحظة الضغط 150 مللي ثم يعود — ويتوقف عن الاستجابة
     تماماً في حالة «جارٍ التحقق»
  3) تذكر آخر مستخدم: يُحفظ في settings (المفتاح last_user) بعد كل دخول
     ناجح، وتُعبّأ القائمة المنسدلة به والمؤشر جاهز في حقل كلمة المرور
  4) شريط قوة كلمة المرور عند التعيين (شاشة إنشاء المدير + تغيير كلمة
     المرور): أحمر أقل من 5 أحرف / برتقالي 5+ / أخضر 6+ وفيها رقم، مع
     نص إرشادي صغير يتغير — والضعيفة جداً تمنع الحفظ برسالة عربية واضحة
  5) اهتزاز البطاقة الوسطية أفقياً نصف ثانية عند رسائل الخطأ مع وميض
     إطار أحمر قصير لحقل كلمة المرور — ورسالة الخطأ النصية تبقى معهما
  6) حالة «جارٍ التحقق...»: نص الزر يتغير ويُعطل الزر ويُمنع الضغط
     المزدوج، مع انتظار 400 مللي قبل عرض النتيجة بإحساس طبيعي —
     والدخول الناجح يكمل فوراً بعدها، وعند الخطأ يعود الزر لحالته
  7) ظهور تدريجي عند الفتح: شفافية ترتفع إلى 1.0 خلال ~300 مللي مع
     انزلاق البطاقة من الأسفل للأعلى قليلاً — ولو لم يدعم النظام alpha
     يُتجاهل بهدوء (try/except) وتظهر النافذة فوراً
  8) صورة خلفية للمحل (اختيارية للمدير من إعدادات الطباعة): filedialog
     تقبل png/jpg وتُحوّل png عبر pillow وتُحفظ باسم ثابت في مجلد البيانات
     ومسارها في settings — وتُعرض خلف بطاقة الدخول بطبقة داكنة شفافة
     فوقها (تُدمج داخل الصورة نفسها) حتى تبقى الحقول واضحة، وأي فشل
     (حذف/تالفة) يُتجاهل بهدوء للخلفية المتدرجة، مع زر إزالة يعيدها
     وتسجيل التعيين/الإزالة في سجل التدقيق

★★★ الإصدار 10 — نظام التحديث التلقائي الصامت (إضافات فقط دون المساس بأي شيء يعمل):
تحديث صامت من مستودع خاص — البائع لا يرى شيئاً اسمه مستودع أو توكن:
  1) فحص تلقائي صامت بعد الدخول مباشرة (after 1500): يجلب رقم الإصدار
     (مهلة 5 ثوانٍ) في خيط خلفي لا يجمّد الواجهة، وأي فشل (لا إنترنت /
     توكن ناقص / مستودع غير موجود) = صمت تام — والنتيجة في سجل التدقيق فقط
  2) شريط إشعار أصفر رفيع أعلى الشريط الإحصائي: «🔔 يتوفر تحديث جديد
     للبرنامج» — البائع يرى «راجع المدير» فقط، والمدير يرى زر
     «⬇️ تحديث الآن» + زر ✕ لإخفاء الشريط لهذه الجلسة
  3) التثبيت (المدير فقط): نافذة تأكيد «يتطلب إعادة تشغيل بعد التثبيت.
     التحديث لا يلمس بياناتك والتقارير نهائياً» ثم خطوات صارمة بالترتيب:
     تنزيل إلى ملف مؤقت main_new.tmp (وليس فوق القديم) ← التحقق من
     السلامة (حجم > 10 كيلوبايت + يحتوي VERSION + يبدأ بتعليق أو import)
     ← نسخة أمان main_backup_[الإصدار].py (يُحتفظ بآخر 3) ← الاستبدال
     باسم مكتشف ديناميكياً من __file__ ← حفظ last_update_date + سجل
     التدقيق ← رسالة «تم التحديث ✅ أغلق البرنامج وافتحه من جديد» مع زر
     «إغلاق الآن» — ولو البرنامج EXE: تنبيه التحديث اليدوي — وكل فشل =
     إلغاء آمن «لم يتغير شيء»
  4) لمسات: سطر «الإصدار» أسفل شاشة الدخول + زر «⬇️ التحديث» في الشريط
     الجانبي للمدير فقط + تلميحات على الزرين الجديدين + زر «🔄 فحص
     التحديثات الآن» في نافذة التحديث

★★★ الإصدار 13 — إصلاح أعطال التحديث الثلاثة + أرشيف الإصدارات:
  العيب 1 (إشعار التحديث لا يظهر إلا بعد إعادة التشغيل): فحص دوري صامت
  كل 30 دقيقة عبر after متكرر يستدعي نفس دالة الفحص القائمة — عند اكتشاف
  إصدار أحدث يظهر الشريط الأصفر فوراً دون إعادة تشغيل ولكل الأدوار، وبلا
  تحديث صمت تام (لا رسائل ولا أي أثر إطلاقاً)، والشريط الذي أُخفي بـ✕ لا
  يعود في نفس الجلسة إلا إذا اكتُشف رقم أحدث فعلياً من رقم الشريط المخفي،
  وبعد تبديل المستخدم فحص صامت واحد للجلسة الجديدة
  العيب 2 (نافذة «عن البرنامج»): مدخل دائم واضح لكل المستخدمين من قائمة
  المستخدم المنسدلة — قيم حقيقية ببدائل آمنة لكل حقل: الإصدار VERSION،
  آخر تحديث ناجح أو «لم يتم تحديث بعد»، حالة التحديث من نتيجة آخر فحص
  بالذاكرة («أحدث إصدار ✅» / «يتوفر تحديث جديد 🔔» / «—»)، تاريخ ووقت
  حيان كل ثانية، مستخدم الجلسة بالدور، مجلد البيانات بخط صغير مع زر نسخ
  📋 + عدد الإصدارات المحفوظة بالأرشيف — بلا أي اتصال شبكي عند الفتح
  العيب 3 (زر «فحص التحديثات الآن» اختفى): عاد في مكانين — داخل الشريط
  الأصفر بجانب «⬇️ تحديث الآن» + دائم الظهور للمدير في قائمة المستخدم —
  برسائل نتيجة عربية دائماً ونص الزر «جارٍ الفحص...» أثناء الفحص ثم يعود
  الأرشيف (versions_archive بجوار البرنامج — أو داخل مجلد البيانات إن كان
  مجلد البرنامج غير قابل للكتابة): خطوة (ج) من التثبيت تحفظ النسخة القديمة
  باسم منظم main_v[الإصدار]_[التاريخ].py، وملفات main_backup_* القديمة
  تُنقل إليه تلقائياً عند بدء التشغيل بصمت (بتسجيل في سجل التدقيق)، ولا
  يُحذف منه أي ملف تلقائياً أبداً — سجل تاريخي كامل، والتكرار بنفس الدقيقة
  يأخذ لاحقة _2 أو _3 بلا استبدال ولا فقدان، ونافذة عرض للمدير فقط: جدول
  بكل الملفات مرتبة من الأحدث (الاسم | الإصدار | تاريخ الحفظ | الحجم
  بالكيلوبايت) + زر فتح مجلد الأرشيف في مستكشف ويندوز + زر استعادة أي
  إصدار بتحذير قوي (تُحفظ النسخة الحالية في الأرشيف أولاً قبل الاستبدال —
  لا فقدان في أي اتجاه) — وكل إجراء (فحص/تثبيت/استعادة/نقل) في سجل التدقيق
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os, sys, traceback
import sqlite3, csv, shutil
from datetime import date, datetime

# ★ إضافة (ميزات 1+3): مكتبات قياسية إضافية — التشفير وتصدير Excel وتهريب XML
import hashlib, zipfile, secrets
from xml.sax.saxutils import escape as _xml_escape
import json   # ★ إضافة (إصدار 8 — الميزة 5): قراءة/كتابة صلاحيات المستخدمين بصيغة JSON

# ═══════════════════════════════════════════════════════════
# ★★★ إضافة (إصدار 6 — نظام الطباعة الحرارية): فحص المكتبات عند بدء التشغيل ★★★
# المكتبات المطلوبة للطباعة فقط: pillow + arabic_reshaper + python-bidi
# (أمر التثبيت: pip install pillow arabic-reshaper python-bidi)
# إن لم تتوفر يبقى البرنامج يعمل بشكل كامل كما هو — أزرار الطباعة تعرض
# رسالة التثبيت العربية فقط، وشاشة الإعدادات تعرض ملاحظة أمر التثبيت
# ═══════════════════════════════════════════════════════════
PRINT_LIBS_OK = False
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    from PIL import Image, ImageDraw, ImageFont
    PRINT_LIBS_OK = True
except Exception:
    arabic_reshaper = None
    get_display = None
    Image = ImageDraw = ImageFont = None

PRINT_LIBS_MSG = (
    "مكتبات الطباعة الحرارية غير مثبتة على هذا الجهاز.\n\n"
    "ثبّتها بهذا الأمر ثم أعد تشغيل البرنامج:\n"
    "pip install pillow arabic-reshaper python-bidi\n\n"
    "البرنامج يعمل بشكل كامل بدونها — الطباعة فقط هي المتوقفة.")

# ═══════════════════════════════════════════════════════════
# ★ إضافة (إصدار 9 — الميزة 8): فحص مستقل لمكتبة pillow لصورة خلفية شاشة
# الدخول — قد تتوفر pillow دون بقية مكتبات الطباعة الحرارية فتبقى ميزة
# الخلفية متاحة، وإن لم تتوفر يُتجاهل كل شيء بهدوء (الخلفية المتدرجة)
# ═══════════════════════════════════════════════════════════
LOGIN_BG_PIL_OK = False
try:
    from PIL import Image as _BGImage, ImageTk as _BGImageTk
    LOGIN_BG_PIL_OK = True
except Exception:
    _BGImage = _BGImageTk = None

# ═══════════════════════════════════════════════════════════
# ★★★ إضافة (إصدار 10 — نظام التحديث التلقائي الصامت): ثوابت أعلى الكود ★★★
# تُعدَّل يدوياً عند الحاجة فقط — طلبات الشبكة كلها بمكتبة urllib.request
# القياسية وحدها، والتوكن لا يظهر في أي واجهة ولا يُسجل في أي لوج إطلاقاً
# ═══════════════════════════════════════════════════════════
import urllib.request   # ★ إضافة (إصدار 10): جلب التحديث — المكتبة القياسية وحدها
import threading        # ★ إضافة (إصدار 10): فحص خلفي لا يجمّد الواجهة أبداً

VERSION = "2.3"         # إصدار البرنامج الحالي — يُقارن برقم version.txt
UPDATE_VERSION_URL = "https://raw.githubusercontent.com/zozoaooc/shop-updates/main/version.txt"
UPDATE_FILE_URL    = "https://raw.githubusercontent.com/zozoaooc/shop-updates/main/main.py"
GITHUB_TOKEN = "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"   # يملؤه المالك يدوياً عند تغييره
# عند توفر التوكن: كل طلب يضيف الترويسة Authorization: Bearer {GITHUB_TOKEN}
# وعند فراغه: يجرّب بدون ترويسة — والفشل في الحالتين صمت تام
UPDATE_CHECK_TIMEOUT = 5      # مهلة فحص رقم الإصدار (ثوانٍ)
UPDATE_DOWNLOAD_TIMEOUT = 30  # مهلة تنزيل ملف التحديث (ثوانٍ)

# ---------- ★ مسار البيانات: بجانب البرنامج دائماً (أو مجلد آمن إذا كان الموقع محمياً) ----------
def data_dir():
    """أولوية: متغير SHOP_DATA_DIR ← مجلد البرنامج/EXE (إن كان قابلاً للكتابة) ← مجلد المستخدم"""
    env = os.environ.get("SHOP_DATA_DIR")
    if env:
        return env
    base = (os.path.dirname(sys.executable) if getattr(sys, "frozen", False)
            else os.path.dirname(os.path.abspath(__file__)))
    if os.path.isdir(base) and os.access(base, os.W_OK):
        return base
    return os.path.join(os.environ.get("APPDATA", os.path.expanduser("~")), "ShopSystem")

DB     = os.path.join(data_dir(), "shop.db")
BACKUP = os.path.join(data_dir(), "shop_backup.db")
ERRLOG = os.path.join(data_dir(), "error_log.txt")
NOTES  = []   # ملاحظات تُعرض مرة واحدة عند بدء التشغيل

def note(msg):
    NOTES.append(msg)

def log_error(val, tb=None):
    """تسجيل أي خطأ في error_log.txt (بأقصى جهد — لا يسبب خطأً جديداً أبداً)"""
    try:
        with open(ERRLOG, "a", encoding="utf-8") as f:
            f.write("\n[" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] ")
            if tb:
                f.write("".join(traceback.format_exception(type(val), val, tb)))
            else:
                f.write(f"{type(val).__name__}: {val}\n")
    except Exception:
        pass

# ---------- الألوان والخطوط ----------
BG, SIDEBAR, ACCENT = "#eef2f7", "#1e293b", "#2563eb"
GREEN, RED, ORANGE = "#16a34a", "#dc2626", "#d97706"
CARD, DARK, GRAY, BORDER = "#ffffff", "#0f172a", "#64748b", "#e2e8f0"
F  = ("Segoe UI", 11)
FB = ("Segoe UI", 11, "bold")
FT = ("Segoe UI", 16, "bold")
FV = ("Segoe UI", 16, "bold")
DAYS_AR = ["الإثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت","الأحد"]

# ★ إصلاح رفض الحفظ: يقبل الأرقام العربية ٠١٢٣ والإنجليزية 0123
AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789")

def today_str(): return date.today().isoformat()

def day_name(d):
    y, m, dd = map(int, d.split("-"))
    return DAYS_AR[date(y, m, dd).weekday()]

def to_num(t):
    """★ يقبل كل صيغ الأرقام: عربية، إنجليزية، فاصلة عربية أو نقطة"""
    try:
        s = str(t).strip().translate(AR_DIGITS)
        s = s.replace("٫", ".").replace("،", ".").replace(",", ".")
        s = s.replace(" ", "").replace("٬", "")
        if s == "":
            return None
        return float(s)
    except (ValueError, TypeError):
        return None

def money(v):
    try:
        return f"{v:,.2f}"
    except (TypeError, ValueError):
        return "0.00"

# ================== قاعدة البيانات ==================
def connect():
    conn = sqlite3.connect(DB, timeout=5)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=5000")
    return conn

def init_db():
    """يجهز/يرقّي القاعدة — ويتعامل بأمان مع قاعدة تالفة أو مقفلة بدل الانهيار الصامت"""
    try:
        os.makedirs(os.path.dirname(DB), exist_ok=True)
    except Exception:
        pass
    try:
        _init_db_inner()
    except sqlite3.DatabaseError as e:
        m = str(e).lower()
        corrupt = any(k in m for k in ("not a database", "malformed", "corrupt"))
        locked  = any(k in m for k in ("locked", "busy", "unable to open"))
        if locked or not corrupt:
            raise   # مقفلة من نسخة أخرى، أو خطأ غير متوقع → يظهر صندوق بدء التشغيل
        bad = DB + ".tainted-" + datetime.now().strftime("%Y%m%d-%H%M%S")
        try:
            shutil.move(DB, bad)
            note(f"⚠ تعذر فتح ملف shop.db (قديم أو تالف).\n\nحُفظ كما هو جانباً باسم:\n{os.path.basename(bad)}\n\nوتم إنشاء قاعدة جديدة. بياناتك القديمة موجودة في ذلك الملف ويمكن استعادتها يدوياً بعد إصلاحه.")
        except Exception:
            pass
        _init_db_inner()

def _init_db_inner():
    with connect() as conn:
        # ★ ترقية تلقائية محسّنة من أي نسخة قديمة
        cols = [r[1] for r in conn.execute("PRAGMA table_info(operations)")]
        if cols and ("cost_price" in cols or "sale_price" in cols or "profit" in cols):
            # عمود سعر البيع في النسخة القديمة: sale_price أو price
            # (بدون هذا البديل كانت بيانات بعض النسخ القديمة تُفقد بصمت)
            price_col = "sale_price" if "sale_price" in cols else ("price" if "price" in cols else None)
            conn.execute("ALTER TABLE operations RENAME TO operations_old")
            conn.execute("""CREATE TABLE operations(
                id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL,
                item_name TEXT NOT NULL, quantity REAL NOT NULL,
                price REAL NOT NULL, total REAL NOT NULL, type TEXT NOT NULL)""")
            if price_col:
                conn.execute(f"""INSERT INTO operations(date,item_name,quantity,price,total,type)
                                SELECT date,item_name,quantity,{price_col},
                                       CASE WHEN type='مرتجع' THEN -abs(quantity*{price_col})
                                            ELSE quantity*{price_col} END, type
                                FROM operations_old""")
            conn.execute("DROP TABLE operations_old")

        cols2 = [r[1] for r in conn.execute("PRAGMA table_info(daily_reports)")]
        if cols2 and ("net_profit" in cols2 or "capital" in cols2):
            # ★ بديل آمن لكل عمود قد ينقص في النسخ القديمة:
            #   ops_count ناقص → نحسبه من جدول العمليات نفسه
            #   net_profit / net_total / أو يُحسب = المبيعات - المرتجعات
            net_col = ("net_profit" if "net_profit" in cols2
                       else "net_total" if "net_total" in cols2
                       else "(total_sales - total_returns)")
            oc = ("ops_count" if "ops_count" in cols2 else
                  "(SELECT COUNT(*) FROM operations WHERE operations.date = daily_reports_old.report_date)")
            ca = "closed_at" if "closed_at" in cols2 else "''"
            ts = "total_sales" if "total_sales" in cols2 else "0"
            tr = "total_returns" if "total_returns" in cols2 else "0"
            conn.execute("ALTER TABLE daily_reports RENAME TO daily_reports_old")
            conn.execute("""CREATE TABLE daily_reports(
                id INTEGER PRIMARY KEY AUTOINCREMENT, report_date TEXT NOT NULL UNIQUE,
                ops_count INTEGER, total_sales REAL, total_returns REAL,
                net_total REAL, closed_at TEXT)""")
            conn.execute(f"""INSERT INTO daily_reports(report_date,ops_count,total_sales,
                            total_returns,net_total,closed_at)
                            SELECT report_date,{oc},{ts},{tr},{net_col},{ca}
                            FROM daily_reports_old""")
            conn.execute("DROP TABLE daily_reports_old")

        conn.execute("""CREATE TABLE IF NOT EXISTS operations(
            id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL,
            item_name TEXT NOT NULL, quantity REAL NOT NULL,
            price REAL NOT NULL, total REAL NOT NULL, type TEXT NOT NULL)""")
        conn.execute("""CREATE TABLE IF NOT EXISTS daily_reports(
            id INTEGER PRIMARY KEY AUTOINCREMENT, report_date TEXT NOT NULL UNIQUE,
            ops_count INTEGER, total_sales REAL, total_returns REAL,
            net_total REAL, closed_at TEXT)""")

        # ★ إضافة (ميزة 1+2): جدولا الإعدادات (كلمة المرور المشفرة) وسجل التدقيق
        conn.execute("""CREATE TABLE IF NOT EXISTS settings(
            key TEXT PRIMARY KEY, value TEXT)""")
        conn.execute("""CREATE TABLE IF NOT EXISTS audit_log(
            id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT,
            username TEXT, action TEXT, details TEXT)""")
        # ★ إضافة (ميزة 5): عمود اسم العميل — ترقية آمنة لا تفقد أي بيانات
        # (فحص جديد بعد الترقية لأن cols الأولى تصبح قديمة بعد إعادة البناء)
        ocols = [r[1] for r in conn.execute("PRAGMA table_info(operations)")]
        if "customer_name" not in ocols:
            conn.execute("ALTER TABLE operations ADD COLUMN customer_name TEXT")
        # ★ إضافة (إصدار 3 — ميزة 3): عمود البائع — ترقية آمنة لا تفقد أي بيانات
        # (العمليات القديمة تبقى بقيمة فارغة وتُعرض «—»)
        ocols = [r[1] for r in conn.execute("PRAGMA table_info(operations)")]
        if "seller_name" not in ocols:
            conn.execute("ALTER TABLE operations ADD COLUMN seller_name TEXT")
        # ★ إضافة (إصدار 3 — ميزة 1): جدول المستخدمين — حساب خاص لكل بائع
        conn.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'بائع',
            active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL)""")

        # ★ إضافة (إصدار 5 — نظام الأنواع الثلاثة): ترقية آمنة لا تفقد أي بيانات —
        # 1) قيم النوع القديمة: عمليات «بيع» تصبح «نقداً» (نفس القيمة الموجبة كما هي)
        conn.execute("UPDATE operations SET type='نقداً' WHERE type='بيع'")
        # 2) عمودان جديدان على daily_reports لفصل الدرج النقدي عن جهاز الشبكة
        dcols = [r[1] for r in conn.execute("PRAGMA table_info(daily_reports)")]
        if "total_cash" not in dcols:
            conn.execute("ALTER TABLE daily_reports ADD COLUMN total_cash REAL DEFAULT 0")
            # التقارير القديمة كلها كانت نقداً: total_cash = total_sales و total_network = 0
            conn.execute("UPDATE daily_reports SET total_cash = COALESCE(total_sales, 0)")
        if "total_network" not in dcols:
            conn.execute("ALTER TABLE daily_reports ADD COLUMN total_network REAL DEFAULT 0")

        # ★ إضافة (إصدار 8 — الميزة 5): عمود الصلاحيات الدقيقة على جدول users —
        # ترقية آمنة لا تفقد أي بيانات: البائعون الحاليون يحصلون تلقائياً على
        # الصلاحية الافتراضية (إضافة عمليات وفواتير فقط)، والمدير يملك كل
        # الصلاحيات دائماً بفضل دوره فلا يتأثر بمحتوى العمود إطلاقاً
        ucols = [r[1] for r in conn.execute("PRAGMA table_info(users)")]
        if "permissions" not in ucols:
            conn.execute("ALTER TABLE users ADD COLUMN permissions TEXT DEFAULT '[\"add_ops\"]'")

def is_closed(d):
    with connect() as conn:
        return conn.execute("SELECT 1 FROM daily_reports WHERE report_date=?", (d,)).fetchone() is not None

def day_totals(d):
    """★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): يرجع
    (عدد العمليات، نقداً، شبكة، المرتجعات، الإجمالي)
    والإجمالي = نقداً + شبكة − المرتجعات"""
    with connect() as conn:
        rows = conn.execute("SELECT * FROM operations WHERE date=?", (d,)).fetchall()
    cash = sum((r["total"] or 0) for r in rows if r["type"] == "نقداً")
    netw = sum((r["total"] or 0) for r in rows if r["type"] == "شبكة")
    rets = -sum((r["total"] or 0) for r in rows if r["type"] == "مرتجع")
    return len(rows), cash, netw, rets, cash + netw - rets

# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 2 — دوال مستقلة جديدة (الميزات 1 إلى 6) ★★★
# ═══════════════════════════════════════════════════════════

# ★ إضافة (ميزة 1+2): المستخدم الحالي — يحدده تسجيل الدخول قبل فتح البرنامج
CURRENT_USER = {"name": "مدير"}

def audit(action, details=""):
    """★ إضافة (ميزة 2): تسجيل إجراء في سجل التدقيق — لا يسبب خطأً أبداً"""
    try:
        with connect() as conn:
            conn.execute("INSERT INTO audit_log(ts,username,action,details) VALUES(?,?,?,?)",
                         (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          CURRENT_USER["name"], action, details))
    except Exception:
        pass

def get_setting(key):
    """★ إضافة (ميزة 1): قراءة قيمة من جدول الإعدادات"""
    with connect() as conn:
        r = conn.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
        return r["value"] if r else None

def set_setting(key, value):
    """★ إضافة (ميزة 1): كتابة قيمة في جدول الإعدادات"""
    with connect() as conn:
        conn.execute("INSERT INTO settings(key,value) VALUES(?,?) "
                     "ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value))

def hash_pwd(salt, pwd):
    """★ إضافة (ميزة 1): كلمة المرور تُخزن مشفرة (SHA-256 مع ملح عشوائي) ولا تُحفظ نصاً أبداً"""
    return hashlib.sha256((salt + str(pwd)).encode("utf-8")).hexdigest()

def parse_date_multi(s):
    """★ إضافة (ميزة 4): يقبل 2025-01-10 أو 10-01-2025 أو 10/01/2025 وبالأرقام العربية
    يرجع التاريخ بصيغة ISO، أو "" للحقل الفارغ، أو None عند الصيغة الخاطئة"""
    s = str(s or "").strip().translate(AR_DIGITS)
    s = s.replace("/", "-").replace(".", "-")
    if s == "":
        return ""
    parts = [p for p in s.split("-") if p != ""]
    if len(parts) != 3:
        return None
    try:
        if len(parts[0]) == 4:                # صيغة السنة أولاً: 2025-01-10
            y, m, dd = int(parts[0]), int(parts[1]), int(parts[2])
        else:                                  # صيغة اليوم أولاً: 10-01-2025
            dd, m, y = int(parts[0]), int(parts[1]), int(parts[2])
        return date(y, m, dd).isoformat()     # يرفض الشهر 13 واليوم 32 تلقائياً
    except ValueError:
        return None

def _col_letter(i):
    """★ إضافة (ميزة 3): حرف عمود Excel (A ثم B ...)"""
    return chr(65 + i) if i < 26 else "A" + chr(65 + i - 26)

def export_xlsx(path, headers, rows, widths, desc="", extra=None):
    """★ إضافة (ميزة 3): تصدير Excel حقيقي (xlsx) بمكتبات بايثون القياسية فقط (zipfile)
    - اتجاه الورقة من اليمين لليسار (rightToLeft) ليفتح بالعربية بشكل صحيح
    - عرض أعمدة مناسب (customWidth) لكل عمود
    - الأرقام تُكتب خلايا رقمية قابلة للجمع والحساب داخل Excel
    - الأصفار العربية داخل النصوص تُهرب (escape) كـXML سليم
    - extra: أسطر ملخص إضافية بعد البيانات (أزواج عنوان/قيمة)"""
    def cell(idx, rnum, val, bold=False):
        ref = f"{_col_letter(idx)}{rnum}"
        s = ' s="1"' if bold else ""     # s="1" = نمط الغامق من styles.xml
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return f'<c r="{ref}"{s}><v>{val}</v></c>'
        txt = _xml_escape(str(val if val is not None else ""))
        return f'<c r="{ref}"{s} t="inlineStr"><is><t>{txt}</t></is></c>'

    parts = ['<row r="1">' + "".join(cell(i, 1, h, True) for i, h in enumerate(headers)) + "</row>"]
    rnum = 2
    for row in rows:
        parts.append(f'<row r="{rnum}">' + "".join(cell(i, rnum, v) for i, v in enumerate(row)) + "</row>")
        rnum += 1
    for label, value in (extra or []):
        parts.append(f'<row r="{rnum}">' + cell(0, rnum, label) + cell(1, rnum, value) + "</row>")
        rnum += 1

    cols_xml = "<cols>" + "".join(
        f'<col min="{i + 1}" max="{i + 1}" width="{w}" customWidth="1"/>'
        for i, w in enumerate(widths)) + "</cols>"
    sheet_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<sheetViews><sheetView rightToLeft="1" workbookViewId="0"/></sheetViews>'
        + cols_xml
        + '<sheetData>' + "".join(parts) + '</sheetData></worksheet>')
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<sheets><sheet name="' + _xml_escape("تقرير") + '" sheetId="1" r:id="rId1"/></sheets></workbook>')
    wb_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
        'Target="worksheets/sheet1.xml"/>'
        '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '
        'Target="styles.xml"/></Relationships>')
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="xl/workbook.xml"/></Relationships>')
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        '</Types>')
    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="2"><font><sz val="11"/><name val="Segoe UI"/></font>'
        '<font><b/><sz val="11"/><name val="Segoe UI"/></font></fonts>'
        '<fills count="2"><fill><patternFill patternType="none"/></fill>'
        '<fill><patternFill patternType="gray125"/></fill></fills>'
        '<borders count="1"><border/></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="2">'
        '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/>'
        '</cellXfs></styleSheet>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", root_rels)
        z.writestr("xl/workbook.xml", workbook_xml)
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        z.writestr("xl/styles.xml", styles_xml)
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)
    audit("تصدير Excel", desc or os.path.basename(path))

# ═════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 3 — نظام المستخدمين (حساب خاص لكل بائع) ★★★
# ═════════════════════════════════════════════════════════
def users_count():
    """★ إضافة (إصدار 3): عدد الحسابات في جدول المستخدمين"""
    with connect() as conn:
        return conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]

def get_user_row(username):
    """★ إضافة (إصدار 3): جلب بيانات حساب باسم المستخدم (أو None إن لم يوجد)"""
    with connect() as conn:
        return conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()

def verify_user_password(row, pwd):
    """★ إضافة (إصدار 3): التحقق من كلمة مرور مستخدم — بنفس دالة hash_pwd الموجودة
    (الصيغة المخزنة في users.password_hash هي: salt$hash)"""
    try:
        salt, digest = (row["password_hash"] or "").split("$", 1)
        return hash_pwd(salt, pwd) == digest
    except ValueError:
        return False

def ensure_users_upgraded():
    """★ إضافة (إصدار 3 — ميزة 1): ترقية تلقائية دون فقدان أي شيء —
    كلمة مرور المدير المخزنة في settings تتحول تلقائياً إلى حساب باسم «مدير»
    بدور مدير، والدخول القديم «دخول كبائع» يُستبدل بالحسابات"""
    if users_count() > 0:
        return
    stored = get_setting("admin_pwd")
    if not stored:
        return    # أول تشغيل فعلاً: ستظهر شاشة إنشاء حساب المدير
    salt = get_setting("pwd_salt") or ""
    with connect() as conn:
        conn.execute("INSERT INTO users(username,password_hash,role,active,created_at) "
                     "VALUES(?,?,?,?,?)",
                     ("مدير", salt + "$" + stored, "مدير", 1,
                      datetime.now().strftime("%Y-%m-%d %H:%M")))
    prev = CURRENT_USER["name"]
    CURRENT_USER["name"] = "النظام"
    audit("ترقية تلقائية", "تحويل كلمة مرور المدير من جدول settings إلى حساب «مدير»")
    CURRENT_USER["name"] = prev

# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 8 — نظام الصلاحيات الدقيق (الميزة 5) ★★★
# ═══════════════════════════════════════════════════════════
# عشر صلاحيات يمنحها المدير لكل مستخدم — والمدير يملك كل الصلاحيات دائماً
# (تظهر له مقفلة في شاشة التعديل، ولا يطلب منه الفحص أبداً)
PERMISSIONS = [
    ("add_ops",        "إضافة عمليات وفواتير"),
    ("close_day",      "إغلاق اليوم"),
    ("delete_op",      "حذف عملية"),
    ("reopen_day",     "إعادة فتح يوم مغلق"),
    ("view_audit",     "عرض سجل التدقيق"),
    ("dashboard",      "لوحة المعلومات"),
    ("perf_report",    "تقرير أداء البائعين"),
    ("backup",         "النسخ والاستعادة"),
    ("print_settings", "إعدادات الطباعة"),
    ("export_reports", "تصدير التقارير (CSV/Excel/PDF)"),
]

def load_user_permissions(username):
    """★ إضافة (إصدار 8 — الميزة 5): قراءة صلاحيات مستخدم من جدول users —
    المدير يملك كل الصلاحيات دائماً، والصلاحيات مخزنة نص JSON داخل العمود
    (والبائع القديم قبل الترقية يحصل تلقائياً على الافتراضية: إضافة العمليات فقط)"""
    row = get_user_row(username)
    if row is None:
        return []
    if row["role"] == "مدير":
        return [k for k, _ in PERMISSIONS]
    try:
        return json.loads(row["permissions"] or "[]")
    except Exception:
        return []

def active_users_list():
    """★ إضافة (إصدار 8 — الميزة 2): المستخدمون المفعّلون لقائمة تسجيل الدخول
    المنسدلة — المدير أولاً ثم الباقي أبجدياً"""
    with connect() as conn:
        rows = conn.execute("SELECT username FROM users WHERE active=1 "
                            "ORDER BY (role='مدير') DESC, username").fetchall()
    return [r[0] for r in rows]

# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 4 — الميزة 5: تلميحات Tooltip خفيفة ★★★
# ═══════════════════════════════════════════════════════════
class Tooltip:
    """★ إضافة (إصدار 4 — ميزة 5): تلميح خفيف بـ Toplevel — يظهر بعد 600 مللي
    ثانية من وقوف المؤشر على الزر ويختفي عند الابتعاد، بخلفية داكنة ونص
    أبيض بخط صغير، وممنوع أن يسبب أي خطأ مهما حدث"""
    def __init__(self, widget, text, delay=600):
        self.widget, self.text, self.delay = widget, text, delay
        self.tipwin, self.after_id = None, None
        try:
            widget.bind("<Enter>", self._schedule, add="+")
            widget.bind("<Leave>", self._hide, add="+")
            widget.bind("<ButtonPress>", self._hide, add="+")
        except Exception:
            pass

    def _schedule(self, _e=None):
        try:
            self._cancel()
            self.after_id = self.widget.after(self.delay, self._show)
        except Exception:
            self.after_id = None

    def _cancel(self):
        try:
            if self.after_id is not None:
                self.widget.after_cancel(self.after_id)
        except Exception:
            pass
        self.after_id = None

    def _show(self):
        try:
            if self.tipwin is not None or not self.text or not self.widget.winfo_exists():
                return
            x = self.widget.winfo_rootx() + self.widget.winfo_width() // 2
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
            self.tipwin = tw = tk.Toplevel(self.widget)
            tw.wm_overrideredirect(True)      # بلا شريط عنوان
            tk.Label(tw, text=self.text, bg=DARK, fg="white", justify="right",
                     font=("Segoe UI", 9), padx=10, pady=5).pack()
            tw.update_idletasks()
            w, h = tw.winfo_reqwidth(), tw.winfo_reqheight()
            sw, sh = tw.winfo_screenwidth(), tw.winfo_screenheight()
            x = max(0, min(x - w // 2, sw - w))   # إبقاؤه داخل حدود الشاشة
            y = max(0, min(y, sh - h))
            tw.wm_geometry(f"+{x}+{y}")
        except Exception:
            self.tipwin = None

    def _hide(self, _e=None):
        try:
            if self.tipwin is not None:
                self.tipwin.destroy()
        except Exception:
            pass
        self.tipwin = None
        self._cancel()

def add_tip(widget, text):
    """★ إضافة (إصدار 4 — ميزة 5): تعليق تلميح على أي عنصر بأمان تام"""
    try:
        Tooltip(widget, text)
    except Exception:
        pass

# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 6 — وحدة الطباعة الحرارية المستقلة ★★★
# طابعة Epson TM-T20III بورق 80mm — أوامر ESC/POS خام عبر winspool.drv
# (OpenPrinter / StartDocPrinter / WritePrinter / EndDocPrinter) بلا أي
# نافذة طباعة. كل دالة داخل try/except: أي فشل يعرض رسالة عربية واضحة
# ويسجل في error_log — دون أي انهيار، والبرنامج يعمل كاملاً بدون الطباعة
# ═══════════════════════════════════════════════════════════
PRINT_WIDTH = 576   # عرض ورق 80mm بالبكسل (المقاس القياسي للطابعات الحرارية 80mm)

def shape_ar(text):
    """★ إضافة (إصدار 6): تشكيل النص العربي حروفًا متصلة (arabic_reshaper)
    ثم ضبط الاتجاه من اليمين لليسار (get_display) — النتيجة حروف متصلة
    مثالية كطباعة الكاشير، والنصوص غير العربية تمر كما هي دون تغيير"""
    try:
        if arabic_reshaper is None or get_display is None:
            return str(text)
        return get_display(arabic_reshaper.reshape(str(text)))
    except Exception:
        return str(text)

def _print_font(size, bold=False):
    """★ إضافة (إصدار 6): تحميل خط الطباعة — خط عربي من ويندوز
    (arial ثم tahoma عبر ImageFont) — وعلى الأجهزة التي لا يوجد فيها خط
    ويندوز يُستخدم أي خط متاح بدلاً منه حتى لا تفشل الطباعة أبداً"""
    windir = os.environ.get("WINDIR", r"C:\Windows")
    names = (["arialbd.ttf", "tahomabd.ttf", "segoeuib.ttf"] if bold
             else ["arial.ttf", "tahoma.ttf", "segoeui.ttf"])
    names += ["arial.ttf", "tahoma.ttf"]     # خط عربي عادي أفضل من غامق مفقود
    for n in names:
        p = os.path.join(windir, "Fonts", n)
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
              else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def _fit_font(text, size, bold, max_w):
    """★ إضافة (إصدار 6): تصغير حجم الخط تلقائياً إن كان النص أعرض من
    الورقة (مثل اسم محل طويل) حتى لا يُقص أي حرف من التقرير المطبوع"""
    try:
        f = _print_font(size, bold)
        gl = getattr(f, "getlength", None)
        if gl is None:
            return f
        while size > 14 and gl(shape_ar(text)) > max_w:
            size -= 2
            f = _print_font(size, bold)
        return f
    except Exception:
        return _print_font(size, bold)

def render_report_image(lines):
    """★ إضافة (إصدار 6): رسم التقرير كصورة عربية سليمة — عرض 576 بكسل
    (ورق 80mm)، خلفية بيضاء ونص أسود، مع تشكيل الحروف المتصلة وضبط
    الاتجاه. كل سطر من الأسطر أحد الأنواع:
      ("title", الاسم)             اسم المحل بخط كبير غامق في المنتصف
      ("head",  النص)              عنوان غامق في المنتصف
      ("center", النص)             سطر عادي في المنتصف
      ("sep", "=")                 سطر فاصل ===== / ("sep", "─") خط مرسوم
      ("row",  العنوان, القيمة)    إحصائية: العنوان يميناً والقيمة يساراً
      ("big",  العنوان, القيمة)    مثل row بخط أكبر (إجمالي اليوم)
      ("blank",)                   فراغ بين المقاطع"""
    W = PRINT_WIDTH
    pad = 16
    heights = {"title": 42, "head": 33, "center": 29, "row": 31,
               "big": 40, "sep": 24, "blank": 14}
    bands, H = [], 10                       # هامش علوي 10 بكسل
    for ln in lines:
        kind = ln[0]
        h = heights.get(kind, 29)
        bands.append((kind, ln, H, h))
        H += h
    H += 26                                  # هامش سفلي قبل قص الورق
    img = Image.new("L", (W, H), 255)        # خلفية بيضاء
    dr = ImageDraw.Draw(img)
    title_txt = lines[0][1] if lines and lines[0][0] == "title" else ""
    f_title  = _fit_font(title_txt, 30, True, W - 2 * pad)
    f_head   = _fit_font(" ".join(str(l[1]) for l in lines if l[0] == "head"),
                         22, True, W - 2 * pad)
    f_center = _print_font(20, False)
    f_row    = _print_font(20, True)
    f_big    = _print_font(27, True)
    f_sep    = _print_font(18, False)
    for kind, ln, y, h in bands:
        cy = y + h / 2
        try:
            if kind == "title":
                dr.text((W / 2, cy), shape_ar(ln[1] or " "), font=f_title, fill=0, anchor="mm")
            elif kind == "head":
                dr.text((W / 2, cy), shape_ar(ln[1] or " "), font=f_head, fill=0, anchor="mm")
            elif kind == "center":
                dr.text((W / 2, cy), shape_ar(ln[1] or " "), font=f_center, fill=0, anchor="mm")
            elif kind == "row":
                dr.text((W - pad, cy), shape_ar(ln[1] or " "), font=f_row, fill=0, anchor="rm")
                dr.text((pad, cy), shape_ar(ln[2] if len(ln) > 2 else ""), font=f_row, fill=0, anchor="lm")
            elif kind == "big":
                dr.text((W - pad, cy), shape_ar(ln[1] or " "), font=f_big, fill=0, anchor="rm")
                dr.text((pad, cy), shape_ar(ln[2] if len(ln) > 2 else ""), font=f_big, fill=0, anchor="lm")
            elif kind == "sep":
                if ln[1] == "─":
                    dr.rectangle([pad + 24, cy - 1, W - pad - 24, cy + 1], fill=0)
                else:
                    dr.text((W / 2, cy), shape_ar(str(ln[1]) * 46), font=f_sep, fill=0, anchor="mm")
            # blank: فراغ فقط — لا رسم فيه
        except Exception:
            pass                    # الرسم لا يسبب أي خطأ أبداً
    return img

def image_to_escpos(img, band_rows=128):
    """★ إضافة (إصدار 6): تحويل الصورة إلى أوامر ESC/POS نقطية (GS v 0) —
    كل بكسل أسود = نقطة طباعة، وتُرسل الصورة على دفعات (حتى 128 صفاً
    نقطياً في كل أمر) كي لا تفيض ذاكرة الطابعة — ترجع بايتات الصورة فقط"""
    gray = img.convert("L")
    w, h = gray.size
    bpr = (w + 7) // 8                    # بايتات كل صف نقطي (576 ÷ 8 = 72)
    raw = gray.tobytes()                  # بايت لكل بكسل: 0 أسود / 255 أبيض
    out = bytearray()
    for y0 in range(0, h, band_rows):
        hh = min(band_rows, h - y0)
        # أمر GS v 0: 1D 76 30 00 ثم عرض الدفعة بالبايتات ثم ارتفاعها
        out += bytes((0x1D, 0x76, 0x30, 0x00, bpr & 0xFF, (bpr >> 8) & 0xFF,
                      hh & 0xFF, (hh >> 8) & 0xFF))
        for y in range(y0, y0 + hh):
            row = bytearray(bpr)
            base = y * w
            for xb in range(bpr):
                b = 0
                x = xb << 3
                for k in range(8):
                    if x + k < w and raw[base + x + k] < 160:   # بكسل داكن = نقطة
                        b |= 0x80 >> k
                row[xb] = b
            out += row
    return bytes(out)

def get_windows_printers():
    """★ إضافة (إصدار 6): جلب قائمة أسماء طابعات ويندوز المثبتة عبر
    EnumPrinters (ctypes) — ترجع قائمة أسماء (قد تكون فارغة) ولا تسبب
    أي خطأ أبداً مهما حدث"""
    try:
        import ctypes
        from ctypes import wintypes
        if os.name != "nt":
            return []
        winspool = ctypes.WinDLL("winspool.drv", use_last_error=True)

        class PRINTER_INFO_1W(ctypes.Structure):
            _fields_ = [("Flags", wintypes.DWORD),
                        ("pDescription", wintypes.LPWSTR),
                        ("pName", wintypes.LPWSTR),
                        ("pComment", wintypes.LPWSTR)]
        needed, returned = wintypes.DWORD(0), wintypes.DWORD(0)
        flags = 2 | 4                     # PRINTER_ENUM_LOCAL | PRINTER_ENUM_CONNECTIONS
        winspool.EnumPrintersW(flags, None, 1, None, 0,
                               ctypes.byref(needed), ctypes.byref(returned))
        if needed.value == 0:
            return []
        size = needed.value
        buf = ctypes.create_unicode_buffer(size)
        if not winspool.EnumPrintersW(flags, None, 1, buf, size,
                                      ctypes.byref(needed), ctypes.byref(returned)):
            return []
        arr = ctypes.cast(buf, ctypes.POINTER(PRINTER_INFO_1W))
        return [arr[i].pName for i in range(returned.value) if arr[i].pName]
    except Exception as e:
        log_error(e)
        return []

def send_raw_to_printer(printer_name, data):
    """★ إضافة (إصدار 6): إرسال أوامر خام (ESC/POS) إلى الطابعة مباشرة عبر
    winspool.drv — OpenPrinter ثم StartDocPrinter (نوع RAW) ثم WritePrinter
    ثم EndDocPrinter — بلا أي نافذة طباعة. يرجع (True, "") عند النجاح أو
    (False, سبب واضح) عند الفشل، ولا يسبب أي انهيار أبداً"""
    try:
        import ctypes
        from ctypes import wintypes
        if os.name != "nt":
            return False, "الإرسال الخام للطابعة يعمل على ويندوز فقط (winspool.drv)"
        winspool = ctypes.WinDLL("winspool.drv", use_last_error=True)
        # تعريف التواقيع لضمان سلامة المؤشرات على أنظمة 32 و64 بت
        winspool.OpenPrinterW.argtypes = [wintypes.LPWSTR,
                                          ctypes.POINTER(wintypes.HANDLE), ctypes.c_void_p]
        winspool.OpenPrinterW.restype = wintypes.BOOL
        winspool.ClosePrinter.argtypes = [wintypes.HANDLE]
        winspool.StartDocPrinterW.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p]
        winspool.StartDocPrinterW.restype = wintypes.BOOL
        winspool.EndDocPrinter.argtypes = [wintypes.HANDLE]
        winspool.EndDocPrinter.restype = wintypes.BOOL
        winspool.StartPagePrinter.argtypes = [wintypes.HANDLE]
        winspool.StartPagePrinter.restype = wintypes.BOOL
        winspool.EndPagePrinter.argtypes = [wintypes.HANDLE]
        winspool.EndPagePrinter.restype = wintypes.BOOL
        winspool.WritePrinter.argtypes = [wintypes.HANDLE, ctypes.c_void_p,
                                          wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
        winspool.WritePrinter.restype = wintypes.BOOL

        class DOC_INFO_1W(ctypes.Structure):
            _fields_ = [("pDocName", wintypes.LPWSTR),
                        ("pOutputFile", wintypes.LPWSTR),
                        ("pDatatype", wintypes.LPWSTR)]
        h = wintypes.HANDLE()
        if not winspool.OpenPrinterW(printer_name, ctypes.byref(h), None):
            raise OSError(f"تعذر فتح الطابعة «{printer_name}» — تأكد أنها موصولة ومثبتة")
        try:
            doc = DOC_INFO_1W("تقرير نظام المبيعات", None, "RAW")
            if not winspool.StartDocPrinterW(h, 1, ctypes.byref(doc)):
                raise OSError("تعذر بدء مهمة الطباعة على الطابعة")
            try:
                if not winspool.StartPagePrinter(h):
                    raise OSError("تعذر بدء صفحة الطباعة")
                try:
                    written = wintypes.DWORD(0)
                    buf = ctypes.create_string_buffer(bytes(data), len(data))
                    if not winspool.WritePrinter(h, buf, len(data), ctypes.byref(written)):
                        raise OSError("تعذر إرسال البيانات إلى الطابعة")
                finally:
                    winspool.EndPagePrinter(h)
            finally:
                winspool.EndDocPrinter(h)
        finally:
            winspool.ClosePrinter(h)
        return True, ""
    except Exception as e:
        log_error(e)
        return False, str(e)

def print_report_lines(printer_name, lines, job_title="تقرير"):
    """★ إضافة (إصدار 6): الطباعة الكاملة للتقرير الحراري — رسم عربي سليم
    ثم أوامر ESC/POS نقطية ثم إرسال خام ثم قص الورق (GS V) بعد كل طباعة.
    كل فشل يعرض رسالة عربية واضحة ويسجل في error_log — وترجع True عند
    نجاح إرسال المهمة إلى الطابعة"""
    try:
        if not PRINT_LIBS_OK:
            messagebox.showerror("الطباعة غير متاحة", PRINT_LIBS_MSG)
            return False
        name = (printer_name or "").strip()
        if not name:
            messagebox.showerror("لا توجد طابعة مختارة",
                "لم يتم اختيار طابعة بعد.\n\n"
                "اختر الطابعة الحرارية من شاشة «⚙️ إعدادات الطباعة» أولاً.")
            return False
        img = render_report_image(lines)
        # ESC @ تهيئة الطابعة ثم الصورة النقطية ثم أمر قص الورق GS V
        data = b"\x1B\x40" + image_to_escpos(img) + b"\x1D\x56\x42\x00"
        ok, err = send_raw_to_printer(name, data)
        if not ok:
            log_error(RuntimeError("فشل الإرسال إلى الطابعة: " + err))
            messagebox.showerror("فشل الطباعة",
                "تعذر طباعة «" + job_title + "».\n"
                "تأكد أن الطابعة موصولة بالكهرباء والكابل ومختارة في الإعدادات.\n\n" + err)
            return False
        return True
    except Exception as e:
        log_error(e, sys.exc_info()[2])
        messagebox.showerror("فشل الطباعة",
            "حدث خطأ أثناء الطباعة:\n\n" + str(e) + "\n\nسُجل الخطأ في error_log.txt")
        return False

def build_day_report_lines(store_name, d, ops_count, cash, netw, rets, net,
                           closed_at, closed_by, reprint=False):
    """★ إضافة (إصدار 6): تجهيز أسطر تقرير إغلاق اليوم بالتنسيق الحراري
    القياسي: اسم المحل ثم ===== ثم العنوان والتاريخ واسم اليوم ووقت
    الإغلاق، الإحصائيات سطراً لكل واحدة ثم ───── ثم الإجمالي بخط أكبر،
    وأسفلها «أغلق بواسطة» وسطر الشكر — والأرقام كلها بصيغة money الموجودة"""
    lines = [
        ("title", store_name or "نظام المبيعات والمُرتجعات"),
        ("sep", "="),
        ("head", "تقرير إغلاق اليوم"),
        ("center", f"{day_name(d)} {d}"),
        ("center", f"وقت الإغلاق: {closed_at or '—'}"),
        ("blank",),
        ("row", "عدد العمليات", str(ops_count)),
        ("row", "مبيعات نقداً", money(cash)),
        ("row", "مبيعات شبكة", money(netw)),
        ("row", "المرتجعات", money(rets)),
        ("sep", "─"),
        ("big", "إجمالي اليوم", money(net)),
        ("blank",),
        ("center", f"أغلق بواسطة: {closed_by or '—'}"),
    ]
    if reprint:                     # إعادة الطباعة: سطر إضافي بالوقت الحالي
        lines.append(("center", "إعادة طباعة — "
                      + datetime.now().strftime("%Y-%m-%d %H:%M")))
    lines += [("blank",), ("center", "شكراً لزيارتكم"), ("blank",)]
    return lines

def build_test_page_lines():
    """★ إضافة (إصدار 6): أسطر صفحة الاختبار القصيرة — اسم النظام وسطر
    تجريبي عربي والتاريخ والوقت — للتأكد أن الطابعة والتشكيل العربي
    يعملان سليماً قبل الاعتماد على الطباعة"""
    t = today_str()
    return [
        ("title", "نظام المبيعات والمُرتجعات"),
        ("sep", "="),
        ("head", "صفحة اختبار الطباعة"),
        ("center", "سطر تجريبي عربي — الحروف متصلة وسليمة"),
        ("center", f"{day_name(t)} {t}"),
        ("center", "الوقت: " + datetime.now().strftime("%H:%M:%S")),
        ("blank",),
        ("center", "شكراً لزيارتكم"),
        ("blank",),
    ]

def get_day_closer(d):
    """★ إضافة (إصدار 6): جلب اسم من أغلق اليوم من سجل التدقيق — ليظهر سطر
    «أغلق بواسطة» صحيحاً عند إعادة طباعة تقرير يوم أغلقه مستخدم آخر"""
    try:
        with connect() as conn:
            r = conn.execute("SELECT username FROM audit_log WHERE action='إغلاق يوم' "
                             "AND details LIKE ? ORDER BY id DESC LIMIT 1",
                             (d + ":%",)).fetchone()
            return r["username"] if r else None
    except Exception:
        return None

# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 7 — الجزء الأول: حماية البيانات بخمس طبقات ★★★
# مجلدات النسخ كلها داخل مجلد backups بجانب البرنامج (نفس مجلد البيانات)
# ═══════════════════════════════════════════════════════════
BACKUP_ROOT       = os.path.join(data_dir(), "backups")
BACKUP_DAILY      = os.path.join(BACKUP_ROOT, "daily")          # 1) النسخ اليومية (آخر 30)
BACKUP_MONTHLY    = os.path.join(BACKUP_ROOT, "monthly")        # 2) النسخ الشهرية (دائمة)
BACKUP_INSTANT    = os.path.join(BACKUP_ROOT, "instant")        # 4) النسخ الفورية (آخر 10)
BACKUP_PRERESTORE = os.path.join(BACKUP_ROOT, "pre_restore")    # نسخ الأمان قبل الاستعادة

def ensure_backup_dirs():
    """★ إضافة (إصدار 7): إنشاء مجلدات النسخ الأربعة عند الحاجة — بأمان تام"""
    for d in (BACKUP_ROOT, BACKUP_DAILY, BACKUP_MONTHLY, BACKUP_INSTANT, BACKUP_PRERESTORE):
        try:
            os.makedirs(d, exist_ok=True)
        except Exception:
            pass

def _sqlite_safe_copy(src, dst):
    """★ إضافة (إصدار 7): نسخ قاعدة بيانات بأمان عبر واجهة sqlite3 الاحتياطية
    (backup API) — نسخة متسقة كاملة حتى مع وجود اتصالات أخرى، وتُحذف أي نسخة
    قديمة بنفس الاسم أولاً. يرجع True/False ولا يسبب أي انهيار أبداً"""
    try:
        if os.path.exists(dst):
            os.remove(dst)
        src_con = sqlite3.connect(src)
        try:
            dst_con = sqlite3.connect(dst)
            try:
                src_con.backup(dst_con)
            finally:
                dst_con.close()
        finally:
            src_con.close()
        return True
    except Exception as e:
        log_error(e)
        try:
            if os.path.exists(dst):
                os.remove(dst)
        except Exception:
            pass
        return False

def prune_backups(folder, prefix, keep):
    """★ إضافة (إصدار 7 — الطبقة 1): الاحتفاظ بآخر «keep» نسخة فقط في مجلد —
    حذف الأقدم تلقائياً (أسماء النسخ تُفرز زمنياً بصيغة التاريخ) ولا يسبب
    أي خطأ أبداً"""
    try:
        names = sorted(n for n in os.listdir(folder)
                       if n.startswith(prefix) and n.endswith(".db"))
        for n in (names[:-keep] if len(names) > keep else []):
            try:
                os.remove(os.path.join(folder, n))
            except Exception:
                pass
    except Exception:
        pass

def make_auto_backup(d):
    """★ إضافة (إصدار 7 — الطبقات 1+2+3): النسخ الاحتياطي التلقائي بعد كل
    «إغلاق يوم» ناجح — نسخة يومية backup_YYYY-MM-DD.db في backups/daily
    (يُحتفظ بآخر 30 فقط) + نسخة شهرية monthly_YYYY-MM.db في backups/monthly
    عند أول إغلاق في الشهر (لا تُحذف أبداً) + كل نسخة يومية وشهرية تُنسخ في
    المكانين معاً (داخلي + خارجي) إن كان المجلد الخارجي مختاراً، وإن فشل
    الخارجي تستمر الداخلية — يرجع قائمة أخطاء (فارغة عند النجاح الكامل)"""
    ensure_backup_dirs()
    errors = []
    daily_path = os.path.join(BACKUP_DAILY, f"backup_{d}.db")
    if _sqlite_safe_copy(DB, daily_path):
        prune_backups(BACKUP_DAILY, "backup_", 30)
        audit("نسخة احتياطية يومية", os.path.basename(daily_path))
    else:
        errors.append("فشل إنشاء النسخة اليومية الداخلية")
    monthly_path = os.path.join(BACKUP_MONTHLY, f"monthly_{d[:7]}.db")
    if not os.path.exists(monthly_path):            # أول إغلاق في هذا الشهر
        if _sqlite_safe_copy(DB, monthly_path):
            audit("نسخة احتياطية شهرية", os.path.basename(monthly_path))
        else:
            errors.append("فشل إنشاء النسخة الشهرية")
    ext = get_setting("external_backup_dir")        # الطبقة 3: المجلد الخارجي
    if ext:
        if not os.path.isdir(ext):      # القرص الخارجي مفصول — تحذير ولا توقف للداخلي
            errors.append(f"المجلد الخارجي غير متوفر: {ext} (هل القرص مفصول؟) — النسخ الداخلية سليمة")
        else:
            for src_path, sub in ((daily_path, "daily"), (monthly_path, "monthly")):
                if os.path.exists(src_path):
                    try:
                        dest = os.path.join(ext, sub)
                        os.makedirs(dest, exist_ok=True)
                        shutil.copy2(src_path, os.path.join(dest, os.path.basename(src_path)))
                        if sub == "daily":
                            prune_backups(dest, "backup_", 30)
                    except Exception as e:
                        log_error(e)
                        errors.append(f"فشل النسخ إلى المجلد الخارجي ({sub}) — النسخ الداخلية سليمة")
    return errors

def make_instant_backup():
    """★ إضافة (إصدار 7 — الطبقة 4): نسخة فورية يدوية instant_YYYY-MM-DD_HHMMSS.db
    في backups/instant — يُحتفظ بآخر 10 فقط — تُسجل في سجل التدقيق وترجع مسارها"""
    ensure_backup_dirs()
    name = "instant_" + datetime.now().strftime("%Y-%m-%d_%H%M%S") + ".db"
    path = os.path.join(BACKUP_INSTANT, name)
    if not _sqlite_safe_copy(DB, path):
        raise RuntimeError("تعذر إنشاء النسخة الفورية — راجع error_log.txt")
    prune_backups(BACKUP_INSTANT, "instant_", 10)
    audit("نسخة فورية", name)
    return path

def check_backup_health(path):
    """★ إضافة (إصدار 7 — الطبقة 4): فحص صحة ملف النسخة قبل الاستعادة —
    محاولة فتحها بـ sqlite3 وقراءة جدول واحد مع فحص سلامة سريع — النسخة
    التالفة تُرفض برسالة واضحة"""
    if not path or not os.path.isfile(path):
        return False, "ملف النسخة غير موجود"
    try:
        con = sqlite3.connect(path)
        try:
            n = con.execute("SELECT COUNT(*) FROM operations").fetchone()[0]
            chk = con.execute("PRAGMA quick_check").fetchone()[0]
        finally:
            con.close()
        if chk != "ok":
            return False, f"فحص السلامة فشل: {chk}"
        return True, f"النسخة سليمة — تحتوي {n} عملية"
    except Exception as e:
        return False, f"نسخة تالفة أو غير قابلة للقراءة:\n{e}"

def count_backup_ops(path):
    """★ إضافة (إصدار 7 — الطبقة 4): عدد العمليات داخل ملف نسخة — تُفتح
    للقراءة فقط عبر sqlite3 مباشرة على الملف دون أي مساس بالقاعدة الحالية"""
    try:
        con = sqlite3.connect(path)
        try:
            return con.execute("SELECT COUNT(*) FROM operations").fetchone()[0]
        finally:
            con.close()
    except Exception:
        return -1

def list_all_backups():
    """★ إضافة (إصدار 7 — الطبقة 4): جمع كل النسخ الداخلية والخارجية في
    قائمة واحدة — النوع والاسم والتاريخ والمكان (داخلي/خارجي/كلاهما) والحجم
    بالكيلوبايت وعدد العمليات داخل كل نسخة — للعرض في شاشة النسخ والاستعادة"""
    ensure_backup_dirs()
    found = {}

    def scan(folder, place):
        try:
            names = sorted(os.listdir(folder))
        except Exception:
            return
        for fname in names:
            if not fname.endswith(".db"):
                continue
            info = found.setdefault(fname, {"name": fname, "internal": False,
                                            "external": False, "path": None,
                                            "size": 0.0, "ops": -1})
            if place == "internal":
                info["internal"] = True
            else:
                info["external"] = True
            if info["path"] is None:
                info["path"] = os.path.join(folder, fname)

    scan(BACKUP_DAILY, "internal")
    scan(BACKUP_MONTHLY, "internal")
    scan(BACKUP_INSTANT, "internal")
    scan(BACKUP_PRERESTORE, "internal")
    ext = get_setting("external_backup_dir")
    if ext:
        scan(os.path.join(ext, "daily"), "external")
        scan(os.path.join(ext, "monthly"), "external")
    out = []
    for info in found.values():
        p = info["path"]
        if p and os.path.isfile(p):
            try:
                info["size"] = round(os.path.getsize(p) / 1024.0, 1)
            except Exception:
                info["size"] = 0.0
            info["ops"] = count_backup_ops(p)
        name = info["name"]
        if name.startswith("backup_"):              # backup_YYYY-MM-DD.db
            info["type"], info["date"] = "يومية", name[7:17]
        elif name.startswith("monthly_"):           # monthly_YYYY-MM.db
            info["type"], info["date"] = "شهرية", name[8:15]
        elif name.startswith("instant_"):           # instant_YYYY-MM-DD_HHMMSS.db
            info["type"], info["date"] = "فورية", name[8:18]
        elif name.startswith("pre_restore_"):       # pre_restore_YYYY-MM-DD_HHMMSS.db
            info["type"], info["date"] = "أمان استعادة", name[12:22]
        else:
            info["type"], info["date"] = "أخرى", ""
        info["place"] = ("كلاهما" if info["internal"] and info["external"]
                         else "داخلي" if info["internal"] else "خارجي")
        out.append(info)
    out.sort(key=lambda x: x["date"], reverse=True)
    return out

def restore_backup_file(path):
    """★ إضافة (إصدار 7 — الطبقة 4): استبدال القاعدة الحالية بملف نسخة —
    أولاً نسخة أمان من الوضع الحالي باسم pre_restore_... ثم استبدال ذري آمن
    (نسخ إلى ملف مؤقت ثم os.replace — لا يبقى ملف نصف مكتوب أبداً). البرنامج
    يستخدم اتصالات قصيرة العمر (with connect()) فلا يوجد اتصال مفتوح يُغلق —
    الاستبدال يتم خارج أي اتصال وبأمان تام. يرجع اسم نسخة الأمان عند النجاح
    ويرفع استثناء قبل أي تغيير إن فشل أي شيء"""
    ensure_backup_dirs()
    safety_name = "pre_restore_" + datetime.now().strftime("%Y-%m-%d_%H%M%S") + ".db"
    safety_path = os.path.join(BACKUP_PRERESTORE, safety_name)
    if not _sqlite_safe_copy(DB, safety_path):
        raise RuntimeError("تعذر إنشاء نسخة الأمان من القاعدة الحالية — أُلغيت الاستعادة للحماية")
    tmp = DB + ".restore_tmp"
    try:
        shutil.copyfile(path, tmp)
        os.replace(tmp, DB)            # استبدال ذري في خطوة واحدة
    except Exception:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except Exception:
            pass
        raise
    return safety_name

def export_xlsx_multi(path, sheets, desc=""):
    """★ إضافة (إصدار 7 — الطبقة 5): نسخة موسعة من export_xlsx الموجودة —
    عدة أوراق في ملف xlsx واحد بنفس منطق zip نفسه دون أي مكتبة خارجية
    إضافية: sheets = [(اسم الورقة, headers, rows, widths), ...] — كل ورقة
    تُبنى بنفس بنية export_xlsx نفسها (RTL + أعمدة بعرض مخصص + خلايا رقمية)"""
    def cell(idx, rnum, val, bold=False):
        ref = f"{_col_letter(idx)}{rnum}"
        s = ' s="1"' if bold else ""
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return f'<c r="{ref}"{s}><v>{val}</v></c>'
        txt = _xml_escape(str(val if val is not None else ""))
        return f'<c r="{ref}"{s} t="inlineStr"><is><t>{txt}</t></is></c>'

    def sheet_xml_of(headers, rows, widths):
        parts = ['<row r="1">' + "".join(cell(i, 1, h, True)
                 for i, h in enumerate(headers)) + "</row>"]
        rnum = 2
        for row in rows:
            parts.append(f'<row r="{rnum}">' +
                         "".join(cell(i, rnum, v) for i, v in enumerate(row)) + "</row>")
            rnum += 1
        cols_xml = "<cols>" + "".join(
            f'<col min="{i + 1}" max="{i + 1}" width="{w}" customWidth="1"/>'
            for i, w in enumerate(widths)) + "</cols>"
        return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                '<sheetViews><sheetView rightToLeft="1" workbookViewId="0"/></sheetViews>'
                + cols_xml + '<sheetData>' + "".join(parts) + '</sheetData></worksheet>')

    n = len(sheets)
    workbook_sheets = "".join(
        f'<sheet name="{_xml_escape(name)}" sheetId="{i + 1}" r:id="rId{i + 1}"/>'
        for i, (name, _h, _r, _w) in enumerate(sheets))
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<sheets>' + workbook_sheets + '</sheets></workbook>')
    wb_rels_items = "".join(
        '<Relationship Id="rId' + str(i + 1) + '" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
        'Target="worksheets/sheet' + str(i + 1) + '.xml"/>' for i in range(n))
    wb_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + wb_rels_items +
        '<Relationship Id="rId' + str(n + 1) + '" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '
        'Target="styles.xml"/></Relationships>')
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="xl/workbook.xml"/></Relationships>')
    overrides = "".join(
        f'<Override PartName="/xl/worksheets/sheet{i + 1}.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        for i in range(n))
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        + overrides +
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        '</Types>')
    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="2"><font><sz val="11"/><name val="Segoe UI"/></font>'
        '<font><b/><sz val="11"/><name val="Segoe UI"/></font></fonts>'
        '<fills count="2"><fill><patternFill patternType="none"/></fill>'
        '<fill><patternFill patternType="gray125"/></fill></fills>'
        '<borders count="1"><border/></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="2">'
        '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/>'
        '</cellXfs></styleSheet>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", root_rels)
        z.writestr("xl/workbook.xml", workbook_xml)
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        z.writestr("xl/styles.xml", styles_xml)
        for i, (_name, headers, rows, widths) in enumerate(sheets):
            z.writestr(f"xl/worksheets/sheet{i + 1}.xml", sheet_xml_of(headers, rows, widths))
    audit("تصدير Excel", desc or os.path.basename(path))

# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 7 — الجزء الثاني: طباعة A4 عبر PDF (reportlab) ★★★
# الحل الجذري لمشكلة الصفحات البيضاء على طابعات A4: التقارير تُنشأ ملفات
# PDF قياسية تفهمها كل الطابعات، بخط عربي مسجل (tahoma/arial) ونفس
# التشكيل العربي الموجود (arabic_reshaper + get_display) — وغياب reportlab
# لا ينهي البرنامج: رسالة عربية بأمر التثبيت فقط (نفس أسلوب الطباعة الحالي)
# ═══════════════════════════════════════════════════════════
PDF_LIBS_OK = False
try:
    from reportlab.lib.pagesizes import A4 as _PDF_A4
    from reportlab.pdfgen import canvas as _pdf_canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont as _PDF_TTFont
    PDF_LIBS_OK = True
except Exception:
    _PDF_A4 = None
    _pdf_canvas = None
    pdfmetrics = None
    _PDF_TTFont = None

PDF_LIBS_MSG = (
    "مكتبة طباعة A4 عبر PDF غير مثبتة على هذا الجهاز.\n\n"
    "ثبّتها بهذا الأمر ثم أعد المحاولة:\n"
    "pip install reportlab\n\n"
    "بقية البرنامج يعمل بشكل كامل بدونها — طباعة A4 فقط هي المتوقفة "
    "(الطباعة الحرارية 80mm تعمل كما هي).")

_pdf_fonts = {}

def ensure_pdf_font():
    """★ إضافة (إصدار 7 — الميزة 6): تسجيل خط عربي في reportlab مرة واحدة —
    tahoma ثم arial (من مجلد خطوط ويندوز) مع بديل آمن لغير ويندوز — يرجع
    اسم الخط أو None إن لم يتوفر أي خط عربي"""
    global _pdf_fonts
    if not PDF_LIBS_OK:
        return None
    if _pdf_fonts:
        return _pdf_fonts.get("regular")
    windir = os.environ.get("WINDIR", r"C:\Windows")
    reg_candidates = [os.path.join(windir, "Fonts", n)
                      for n in ("tahoma.ttf", "arial.ttf", "segoeui.ttf")]
    reg_candidates.append("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    bold_candidates = [os.path.join(windir, "Fonts", n)
                       for n in ("tahomabd.ttf", "arialbd.ttf", "segoeuib.ttf")]
    bold_candidates.append("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    chosen_reg = chosen_bold = None
    for p in reg_candidates:
        if os.path.isfile(p):
            try:
                pdfmetrics.registerFont(_PDF_TTFont("ArabicPDF", p))
                chosen_reg = "ArabicPDF"
                break
            except Exception:
                pass
    for p in bold_candidates:
        if os.path.isfile(p):
            try:
                pdfmetrics.registerFont(_PDF_TTFont("ArabicPDFB", p))
                chosen_bold = "ArabicPDFB"
                break
            except Exception:
                pass
    if chosen_reg is None:
        return None
    _pdf_fonts = {"regular": chosen_reg,
                  "bold": chosen_bold or chosen_reg}   # الغامق المفقود يُستبدل بالعادي
    return chosen_reg

def pdf_font(bold=False):
    """★ إضافة (إصدار 7): اسم خط PDF العربي (العادي أو الغامق) بعد التسجيل"""
    if ensure_pdf_font() is None:
        return None
    return _pdf_fonts["bold"] if bold else _pdf_fonts["regular"]

def build_day_report_pdf(path, store_name, d, ops_count, cash, netw, rets, net,
                         closed_at, closed_by):
    """★ إضافة (إصدار 7 — الميزة 6+8): تقرير إغلاق اليوم كملف PDF مقاس A4
    قياسي — تفهمه كل الطابعات (الحل الجذري للصفحات البيضاء) — بنفس محتوى
    التقرير الحراري تماماً: اسم المحل ثم العنوان والتاريخ واسم اليوم ووقت
    الإغلاق ثم الإحصائيات ثم الإجمالي بخط أكبر ثم «أغلق بواسطة» والشكر"""
    font = ensure_pdf_font()
    if font is None:
        raise RuntimeError("لم يتم العثور على خط عربي (tahoma / arial) لتوليد ملف PDF")
    W, H = _PDF_A4                    # 595.27 × 841.89 نقطة
    c = _pdf_canvas.Canvas(path, pagesize=_PDF_A4)
    M = 56                            # هامش الصفحة

    def ar(x, y, t, size=11, bold=False, align="c", col=(0.06, 0.09, 0.16)):
        c.setFont(pdf_font(bold), size)
        c.setFillColorRGB(*col)
        s = shape_ar(t)               # نفس التشكيل العربي الموجود
        if align == "c":
            c.drawCentredString(x, y, s)
        elif align == "l":
            c.drawString(x, y, s)
        else:
            c.drawRightString(x, y, s)

    y = H - 92
    ar(W / 2, y, store_name or "نظام المبيعات والمُرتجعات", 24, True, "c", (0.09, 0.16, 0.38))
    y -= 18
    c.setStrokeColorRGB(0.55, 0.62, 0.72); c.setLineWidth(1); c.line(M, y, W - M, y)
    y -= 42
    ar(W / 2, y, "تقرير إغلاق اليوم", 19, True)
    y -= 26
    ar(W / 2, y, f"{day_name(d)} {d}", 12, False, "c", (0.36, 0.42, 0.50))
    y -= 20
    ar(W / 2, y, f"وقت الإغلاق: {closed_at or '—'}", 11, False, "c", (0.36, 0.42, 0.50))
    y -= 36
    for label, val in (("عدد العمليات", str(ops_count)),
                       ("مبيعات نقداً", money(cash)),
                       ("مبيعات شبكة", money(netw)),
                       ("المرتجعات", money(rets))):
        ar(W - M - 6, y, label, 13, True, "r")
        ar(M + 6, y, val, 13, False, "l")
        y -= 10
        c.setStrokeColorRGB(0.88, 0.91, 0.95); c.setLineWidth(0.7)
        c.line(M + 44, y, W - M - 44, y)
        y -= 27
    y -= 10
    c.setFillColorRGB(0.87, 0.92, 1.0)     # خلفية زرقاء فاتحة لصف الإجمالي
    c.rect(M, y - 13, W - 2 * M, 40, fill=1, stroke=0)
    ar(W - M - 12, y, "إجمالي اليوم", 16, True, "r")
    ar(M + 12, y, money(net), 16, True, "l",
       (0.02, 0.45, 0.24) if net >= 0 else (0.75, 0.08, 0.08))
    y -= 62
    ar(W / 2, y, f"أغلق بواسطة: {closed_by or '—'}", 12)
    y -= 28
    c.setStrokeColorRGB(0.55, 0.62, 0.72); c.setLineWidth(1); c.line(M, y, W - M, y)
    ar(W / 2, y - 18, "شكراً لزيارتكم", 11, False, "c", (0.36, 0.42, 0.50))
    ar(W / 2, 42, "أُنشئ بواسطة نظام المبيعات والمُرتجعات — "
       + datetime.now().strftime("%Y-%m-%d %H:%M"), 8, False, "c", (0.6, 0.64, 0.7))
    c.showPage()
    c.save()
    return path

def build_period_report_pdf(path, store_name, d_from, d_to, rows):
    """★ إضافة (إصدار 7 — الميزة 8): تقرير الفترة كملف PDF مقاس A4 بعنوان
    «تقرير فترة من [من] إلى [إلى]» — جدول الأيام (التاريخ/عدد العمليات/
    نقداً/شبكة/المرتجعات/الإجمالي) وصف الإجمالي التراكمي أسفله، مع ترقيم
    صفحات تلقائي إذا زادت الأيام عن صفحة واحدة"""
    font = ensure_pdf_font()
    if font is None:
        raise RuntimeError("لم يتم العثور على خط عربي (tahoma / arial) لتوليد ملف PDF")
    W, H = _PDF_A4
    M = 42
    c = _pdf_canvas.Canvas(path, pagesize=_PDF_A4)
    # أعمدة الجدول من اليمين لليسار: التاريخ | عدد العمليات | نقداً | شبكة | المرتجعات | الإجمالي
    col_titles = ["التاريخ", "عدد العمليات", "نقداً", "شبكة", "المرتجعات", "الإجمالي"]
    col_w = [88, 66, 82, 82, 82, 96]
    xs = []                                 # حدود كل عمود (من اليمين إلى اليسار)
    x = W - M
    for wd in col_w:
        xs.append((x - wd, x))
        x -= wd

    def ar(cx, cy, t, size=11, bold=False, align="c", col=(0.06, 0.09, 0.16)):
        c.setFont(pdf_font(bold), size)
        c.setFillColorRGB(*col)
        s = shape_ar(t)
        if align == "c":
            c.drawCentredString(cx, cy, s)
        elif align == "l":
            c.drawString(cx, cy, s)
        else:
            c.drawRightString(cx, cy, s)

    page_no = [1]

    def footer():
        ar(W / 2, 30, f"صفحة {page_no[0]}", 9, False, "c", (0.6, 0.64, 0.7))

    def head_block(first):
        y = H - 78
        if first:
            ar(W / 2, y, store_name or "نظام المبيعات والمُرتجعات", 20, True, "c", (0.09, 0.16, 0.38))
            y -= 26
        ar(W / 2, y, f"تقرير فترة من {d_from} إلى {d_to}", 17, True)
        y -= 20
        ar(W / 2, y, f"عدد الأيام: {len(rows)}", 11, False, "c", (0.36, 0.42, 0.50))
        y -= 28
        c.setFillColorRGB(0.09, 0.16, 0.24)          # رأس الجدول بخلفية داكنة
        c.rect(M, y - 7, W - 2 * M, 26, fill=1, stroke=0)
        for i, t in enumerate(col_titles):
            ar((xs[i][0] + xs[i][1]) / 2, y, t, 10.5, True, "c", (1, 1, 1))
        return y - 33

    y = head_block(True)
    tot_ops, tot_cash, tot_netw, tot_rets, tot_net = 0, 0.0, 0.0, 0.0, 0.0
    for idx, r in enumerate(rows):
        if y < 84:                                    # صفحة جديدة عند الامتلاء
            footer()
            c.showPage()
            page_no[0] += 1
            y = head_block(False)
        cash, netw = r["total_cash"] or 0, r["total_network"] or 0
        rets, net = r["total_returns"] or 0, r["net_total"] or 0
        if idx % 2 == 1:                              # تظليل متناوب للصفوف
            c.setFillColorRGB(0.955, 0.968, 0.984)
            c.rect(M, y - 6, W - 2 * M, 24, fill=1, stroke=0)
        vals = [r["report_date"], str(r["ops_count"] or 0), money(cash),
                money(netw), money(rets), money(net)]
        for i, v in enumerate(vals):
            ar((xs[i][0] + xs[i][1]) / 2, y, v, 10, i == 5 and net < 0, "c",
               (0.75, 0.08, 0.08) if (i == 5 and net < 0) else (0.06, 0.09, 0.16))
        tot_ops += r["ops_count"] or 0
        tot_cash += cash; tot_netw += netw; tot_rets += rets; tot_net += net
        y -= 24
    if y < 84:                                        # صف الإجمالي في صفحة جديدة إذا لزم
        footer()
        c.showPage()
        page_no[0] += 1
        y = head_block(False)
    c.setFillColorRGB(0.87, 0.92, 1.0)                # صف الإجمالي التراكمي
    c.rect(M, y - 7, W - 2 * M, 28, fill=1, stroke=0)
    tot_vals = ["الإجمالي التراكمي", str(tot_ops), money(tot_cash), money(tot_netw),
                money(tot_rets), money(tot_net)]
    for i, v in enumerate(tot_vals):
        ar((xs[i][0] + xs[i][1]) / 2, y, v, 10.5, True, "c",
           (0.02, 0.35, 0.20) if (i == 5 and tot_net >= 0)
           else ((0.75, 0.08, 0.08) if i == 5 else (0.06, 0.09, 0.16)))
    y -= 42
    ar(W / 2, y, f"طُبع بواسطة: {CURRENT_USER['name']}", 10, False, "c", (0.36, 0.42, 0.50))
    footer()
    c.showPage()
    c.save()
    return path

def send_pdf_to_printer(path):
    """★ إضافة (إصدار 7 — الميزة 7): إرسال ملف PDF إلى الطباعة عبر حوار
    الطباعة القياسي في ويندوز — os.startfile بخيار print ثم ShellExecuteW
    — المستخدم يختار طابعة A4 من حوار ويندوز نفسه فتختفي مشكلة الصفحات
    البيضاء نهائياً. يرجع (True, "") أو (False, سبب) مع فتح الملف كحل أخير"""
    try:
        os.startfile(path, "print")            # حوار الطباعة القياسي (ويندوز)
        return True, ""
    except Exception as e1:
        try:
            if os.name == "nt":
                import ctypes
                ctypes.windll.shell32.ShellExecuteW(None, "print", path, None, None, 1)
                return True, ""
            raise OSError(str(e1))
        except Exception as e2:
            try:
                os.startfile(path)             # حل أخير: فتح الملف ليُطبع يدوياً
            except Exception:
                pass
            return False, f"تعذر فتح حوار الطباعة تلقائياً ({e2})"

def build_period_report_lines(store_name, d_from, d_to, rows):
    """★ إضافة (إصدار 7 — الميزة 7+8): أسطر تقرير الفترة للطابعة الحرارية —
    بنفس أسلوب build_day_report_lines الموجود: ترويسة وعنوان ومدى الفترة
    ثم سطر لكل يوم (التاريخ: الإجمالي) ثم الإحصائيات التراكمية بخط أكبر"""
    lines = [
        ("title", store_name or "نظام المبيعات والمُرتجعات"),
        ("sep", "="),
        ("head", "تقرير فترة"),
        ("center", f"من {d_from} إلى {d_to}"),
        ("center", f"عدد الأيام: {len(rows)}"),
        ("blank",),
    ]
    tot_ops, tot_cash, tot_netw, tot_rets, tot_net = 0, 0.0, 0.0, 0.0, 0.0
    for r in rows:
        cash, netw = r["total_cash"] or 0, r["total_network"] or 0
        rets, net = r["total_returns"] or 0, r["net_total"] or 0
        tot_ops += r["ops_count"] or 0
        tot_cash += cash; tot_netw += netw; tot_rets += rets; tot_net += net
        lines.append(("row", r["report_date"], money(net)))
    lines += [
        ("sep", "─"),
        ("row", "عدد العمليات", str(tot_ops)),
        ("row", "نقداً", money(tot_cash)),
        ("row", "شبكة", money(tot_netw)),
        ("row", "المرتجعات", money(tot_rets)),
        ("sep", "─"),
        ("big", "الإجمالي التراكمي", money(tot_net)),
        ("blank",),
        ("center", f"طُبع بواسطة: {CURRENT_USER['name']}"),
        ("center", "شكراً لزيارتكم"),
        ("blank",),
    ]
    return lines

# ================== التطبيق ==================
# ═══════════════════════════════════════════════════════════
# ★★★ إضافة (إصدار 10 — نظام التحديث التلقائي الصامت): دوال مستقلة ★★★
# لا تلمس هذه الدوال أي دالة أو شاشة قائمة، وكل فشل فيها صمت تام:
# البرنامج يعمل طبيعياً 100% كأن لا شيء حصل
# ═══════════════════════════════════════════════════════════

def _update_headers():
    """ترويسات طلب التحديث — عند توفر التوكن يُضاف لكل طلب، والتوكن لا
    يظهر في أي واجهة ولا يُسجل في أي لوج إطلاقاً"""
    h = {"User-Agent": "ShopSystem-Update"}
    if GITHUB_TOKEN.strip():
        h["Authorization"] = "Bearer " + GITHUB_TOKEN.strip()
    return h

def update_fetch(url, timeout=5):
    """جلب محتوى رابط التحديث بمكتبة urllib.request القياسية وحدها —
    أي فشل (لا إنترنت / توكن ناقص / مستودع غير موجود) يرجع None بصمت تام"""
    try:
        req = urllib.request.Request(url, headers=_update_headers())
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception:
        return None

def update_fetch_async(url, timeout=5):
    """بدء الجلب في خيط خلفي كي لا تتجمد الواجهة ولو كانت الشبكة بطيئة —
    يرجع صندوق حالة يستطلعه الخيط الرئيسي بـ after فقط، فالخيط الخلفي
    لا يلمس Tk إطلاقاً (الطريقة القياسية الآمنة للشبكة مع الواجهة)"""
    box = {"state": "busy", "data": None}
    def _work():
        try:
            box["data"] = update_fetch(url, timeout)
        finally:
            box["state"] = "done"
    try:
        threading.Thread(target=_work, daemon=True).start()
    except Exception:                    # تعذر فتح خيط (نادر جداً): جلب مباشر
        box["data"] = update_fetch(url, timeout)
        box["state"] = "done"
    return box

def update_parse_version(raw):
    """قراءة رقم الإصدار من محتوى version.txt — None عند أي خلل في المحتوى
    ★ إصلاح (11 — البند أ): الرقم غير القابل للقراءة (أحرف، رموز، صفحة
    خطأ HTML) = None دائماً — لا شريط ولا زر إطلاقاً إلا لرقم نظيف أرقام
    ونقاط فقط، فالمقارنة أرقام حقيقية ولا معنى لمقارنة نص غير رقمي"""
    try:
        t = raw.decode("utf-8").strip()
    except Exception:
        return None
    if not t or len(t) > 12 or "\n" in t:
        return None
    parts = t.split(".")
    return t if parts and all(p.isdigit() and len(p) <= 4 for p in parts) else None

def update_is_newer(remote, local):
    """مقارنة رقمي إصدار جزءاً جزءاً بأرقام حقيقية لا نصوص (2.10 أحدث من
    2.9 و 10.0 أحدث من 9.9 و 2.0.2 أحدث من 2.0)
    ★ إصلاح (11 — البند أ): صارمة تماماً — (1) تسوية الطول بالأصفار قبل
    المقارنة كي تُعدّ 2.0.0 مساويةً لـ 2.0 لا أحدث منها (2) عند أي استثناء
    أو خلل النتيجة False (ليست أحدث) — «مختلف عن المحلي» لم يعد يعني
    «أحدث» أبداً، فالشريط والزر لا يظهران إلا إذا كان رقم المستودع أكبر
    من VERSION المحلي فعلياً جزءاً جزءاً"""
    def _parts(v):
        out = []
        for p in str(v).strip().split("."):
            p = p.strip()
            out.append(int(p) if p.isdigit() else 0)
        return out or [0]
    try:
        rp, lp = _parts(remote), _parts(local)
        n = max(len(rp), len(lp))       # تسوية الطول بالأصفار ثم مقارنة رقمية
        rp += [0] * (n - len(rp))
        lp += [0] * (n - len(lp))
        return rp > lp                   # أحدث فقط إذا أكبر رقماً فعلياً
    except Exception:
        return False                     # غير قابل للمقارنة = ليس أحدث

def update_check_silent(app, quiet=False):
    """(1) الفحص التلقائي الصامت بعد الدخول مباشرة — لا يبطئ الفتح ولا
    يظهر شيئاً أثناءه: يجلب رقم الإصدار بمهلة 5 ثوانٍ، وأي فشل صمت تام
    (البرنامج يعمل طبيعياً 100%)، والنتيجة تُسجل في سجل التدقيق فقط
    بصمت — وعند توفر إصدار جديد يظهر شريط الإشعار الأصفر وحده دون أي
    تفاصيل تقنية
    ★ تعديل مصرح به (إصلاح 1 — الفحص الدوري): إضافة معامل اختياري
    quiet=False وحده — عند True (الفحص الدوري كل 30 دقيقة) يكون الصمت
    تاماً تماماً: لا رسائل ولا أي أثر ولا سطر في سجل التدقيق عند غياب
    تحديث أحدث أو فشل الاتصال، ولا يُسجل في سجل التدقيق إلا اكتشافُ
    إصدار جديد فعلياً. السلوك الافتراضي (quiet=False) كما كان حرفياً
    لكل النداءات القائمة، ونتيجة آخر فحص ختامية تُحفظ في الذاكرة
    (update_last_check_result) في كل الأحوال لنافذة «عن البرنامج»"""
    box = update_fetch_async(UPDATE_VERSION_URL, UPDATE_CHECK_TIMEOUT)
    def _poll():
        if box["state"] != "done":
            try:
                app.after(250, _poll)
            except Exception:
                pass
            return
        remote = update_parse_version(box["data"] or b"")
        if remote is None:      # لا إنترنت / توكن ناقص / مستودع غير موجود
            if not quiet:       # الفحص الدوري: الفشل صمت تام بلا أي أثر
                audit("فحص تحديث تلقائي", "تعذر الوصول للمصدر — تجاهل بهدوء")
            return
        if not update_is_newer(remote, VERSION):
            app.update_last_check_result = "latest"   # لنافذة «عن البرنامج»
            if not quiet:       # الفحص الدوري بلا تحديث: صمت تام لا أي أثر
                audit("فحص تحديث تلقائي", f"أحدث إصدار ({VERSION})")
            return
        app.update_available_version = remote
        app.update_last_check_result = "available"
        audit("فحص تحديث تلقائي", f"يتوفر إصدار جديد: {remote}"
              + (" — فحص دوري" if quiet else ""))
        try:
            app.refresh_update_bar()
        except Exception:
            pass
    try:
        app.after(250, _poll)
    except Exception:
        pass


# ═══════════════════════════════════════════════════════════
# ★★★ إضافة (أرشيف الإصدارات): مجلد versions_archive بجوار البرنامج ★★★
# سجل تاريخي كامل لكل إصدارات البرنامج المحفوظة — لا يُحذف منه أي ملف
# تلقائياً أبداً: خطوة (ج) من التثبيت تحفظ النسخة القديمة هنا باسم منظم،
# وملفات main_backup_* القديمة تُنقل إليه عند بدء التشغيل، والاستعادة
# تحفظ النسخة الحالية هنا أولاً — لا فقدان في أي اتجاه
# ═══════════════════════════════════════════════════════════

def archive_dir():
    """مجلد أرشيف الإصدارات versions_archive — بجوار البرنامج دائماً، وإن
    كان مجلد البرنامج غير قابل للكتابة يُنشأ داخل مجلد البيانات data_dir()
    (بنفس أولويات مسار البيانات القائم)، ويُنشأ تلقائياً عند أول حاجة"""
    env = os.environ.get("SHOP_DATA_DIR")
    if env:
        base = env
    else:
        base = (os.path.dirname(sys.executable) if getattr(sys, "frozen", False)
                else os.path.dirname(os.path.abspath(__file__)))
        if not (os.path.isdir(base) and os.access(base, os.W_OK)):
            return os.path.join(data_dir(), "versions_archive")
    folder = os.path.join(base, "versions_archive")
    try:
        os.makedirs(folder, exist_ok=True)     # يُنشأ تلقائياً عند أول حاجة
    except Exception:
        pass
    return folder

def archive_unique_path(folder, name):
    """مسار فريد داخل الأرشيف: نفس الاسم بنفس الدقيقة يأخذ لاحقة _2 أو _3
    — لا استبدال ولا فقدان أبداً (الأرشيف سجل تاريخي كامل)"""
    p = os.path.join(folder, name)
    if not os.path.exists(p):
        return p
    root, ext = os.path.splitext(name)
    n = 2
    while os.path.exists(os.path.join(folder, f"{root}_{n}{ext}")):
        n += 1
    return os.path.join(folder, f"{root}_{n}{ext}")

def archive_prog_root():
    """الاسم الأساسي لملف البرنامج (main عادةً) — تسمية ملفات الأرشيف
    main_v[الإصدار]_[التاريخ].py تتبعه أياً كان اسم الملف الفعلي"""
    try:
        return os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
    except Exception:
        return "main"

def archive_save_current():
    """حفظ الكود الحالي في الأرشيف باسم منظم main_v[الإصدار]_[التاريخ].py
    (مثال: main_v2.0_2025-01-15_1430.py) — يرجع مسار الملف المحفوظ أو
    None عند أي فشل (بلا أي أثر جانبي إطلاقاً)"""
    try:
        target = os.path.abspath(__file__)
        if not os.path.isfile(target):
            return None
        name = (archive_prog_root() + "_v" + VERSION + "_"
                + datetime.now().strftime("%Y-%m-%d_%H%M") + ".py")
        dest = archive_unique_path(archive_dir(), name)
        shutil.copy2(target, dest)
        return dest
    except Exception:
        return None

def archive_file_version(path):
    """قراءة رقم الإصدار لملف من الأرشيف: من اسمه أولاً (main_v2.0_...)،
    وإن لم يكن بالاسم تُقرأ أول أسطر الملف نفسه بحثاً عن سطر VERSION —
    و«—» عند تعذر الاثنين"""
    stem = os.path.splitext(os.path.basename(path))[0]
    try:
        if "_v" in stem:
            ver = stem.split("_v", 1)[1].split("_", 1)[0]
            if ver and all(p.isdigit() for p in ver.split(".")):
                return ver
    except Exception:
        pass
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for _ in range(80):
                ln = f.readline()
                if not ln:
                    break
                ln = ln.strip()
                if ln.startswith("VERSION") and "=" in ln:
                    v = ln.split("=", 1)[1].strip().strip('"').strip("'")
                    if v and len(v) <= 12 and all(p.isdigit() for p in v.split(".")):
                        return v
    except Exception:
        pass
    return "—"

def archive_count():
    """عدد ملفات الإصدارات المحفوظة في الأرشيف (لنافذة «عن البرنامج»)"""
    try:
        return len([p for p in os.listdir(archive_dir()) if p.endswith(".py")])
    except Exception:
        return 0

def archive_list_files():
    """كل ملفات الأرشيف مرتبة من الأحدث إلى الأقدم — كل ملف: (الاسم،
    الإصدار، تاريخ الحفظ، الحجم بالكيلوبايت، المسار)"""
    out = []
    try:
        names = [p for p in os.listdir(archive_dir()) if p.endswith(".py")]
    except Exception:
        return out
    for name in names:
        path = os.path.join(archive_dir(), name)
        try:
            st = os.stat(path)
            out.append({"name": name, "path": path,
                        "version": archive_file_version(path),
                        "saved": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M"),
                        "size_kb": f"{st.st_size / 1024:.1f}",
                        "mtime": st.st_mtime})
        except Exception:
            continue
    out.sort(key=lambda r: r["mtime"], reverse=True)    # الأحدث أولاً
    return out

def archive_migrate_old_backups():
    """نقل ملفات main_backup_* القديمة بجوار البرنامج إلى versions_archive
    عند بدء التشغيل مرة واحدة بصمت — يُنظف مجلد البرنامج من فوضى الماضي،
    والنقل يُسجل في سجل التدقيق (بأقصى جهد — لا يسبب خطأً أبداً)"""
    try:
        base = (os.path.dirname(sys.executable) if getattr(sys, "frozen", False)
                else os.path.dirname(os.path.abspath(__file__)))
        if not os.path.isdir(base):
            return
        prefix = archive_prog_root() + "_backup_"
        olds = [p for p in os.listdir(base)
                if p.startswith(prefix) and p.endswith(".py")]
        if not olds:
            return
        moved = []
        for name in olds:
            try:
                dest = archive_unique_path(archive_dir(), name)
                shutil.move(os.path.join(base, name), dest)
                moved.append(name)
            except Exception:
                pass
        if moved:
            audit("أرشيف الإصدارات",
                  "نُقلت نسخ الأمان القديمة إلى الأرشيف: " + "، ".join(moved))
    except Exception:
        pass


class App(tk.Tk):
    def __init__(self, role="مدير", user_name="مدير"):
        # ★ تعديل ضروري معلن (ميزة 1): إضافة معلمة الدور لتستقبل نتيجة نافذة الدخول
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 2): إضافة معلمة اسم المستخدم الحالي
        # القيم الافتراضية تحافظ على السلوك القديم عند البناء بدون معاملات
        super().__init__()
        self.title("نظام المبيعات والمرتجعات — محل الكمبيوتر")
        # ★ تعديل ضروري معلن (إصدار 10 — نظام التحديث): رفع الارتفاع الافتراضي
        # من 700 إلى 760 فقط — الشريط الجانبي كان ممتلئاً بالكامل (آخر زر
        # قائم ينتهي عند 637 من 700) وزر «التحديث» الجديد للمدير يحتاج
        # مساحته دون قصّ أي زر قائم؛ الحد الأدنى للتصغير بقي كما هو (950×620)
        self.geometry("1100x760"); self.minsize(950, 620)
        self.configure(bg=BG)
        init_db()
        # ★ إضافة (إصدار 6): فحص مكتبات الطباعة عند بدء التشغيل — إن لم تتوفر
        # والطباعة معدّة مسبقاً (طابعة محفوظة أو طباعة تلقائية مفعلة) تظهر
        # ملاحظة عربية بأمر التثبيت مع ملاحظات بدء التشغيل، والبرنامج يعمل
        # طبيعياً تماماً — وبلا أي إعداد للطباعة لا تظهر أي رسالة إزعاج
        try:
            if not PRINT_LIBS_OK and (get_setting("printer_name") or
                                      get_setting("auto_print_daily") == "1"):
                note("⚠ الطباعة الحرارية غير متاحة في هذا التشغيل.\n\n" + PRINT_LIBS_MSG)
        except Exception:
            pass
        self.role = role          # ★ إضافة (ميزة 1): دور المستخدم الحالي (مدير/بائع)
        self.user_name = user_name   # ★ إضافة (إصدار 3 — ميزة 2): اسم المستخدم الحالي
        self.user_role = role         # ★ إضافة (إصدار 3 — ميزة 2): دور المستخدم الحالي
        # ★ إضافة (إصدار 8 — الميزة 3): قائمة التتبع المركزية لكل نافذة Toplevel
        # تُفتح (تفاصيل اليوم، المعاينة، إدارة المستخدمين، تغيير كلمة المرور...)
        # — تُغلق كلها فوراً عند تبديل المستخدم
        self.open_windows = []
        # ★ إصلاح (11 — البند ب): علم حالة التحديث مخفي افتراضياً عند بدء
        # التشغيل — لا شريط ولا زر تحديث مهما كان المستودع إلا من داخل
        # نتيجة مقارنة ناجحة تثبت وجود إصدار أحدث من VERSION فعلياً
        self.update_available_version = None   # لا تحديث مؤكد عند الإقلاع
        self.update_bar = None                 # لا شريط إشعار عند الإقلاع
        self.update_bar_dismissed = False      # لم يُخفِ المدير شيئاً بعد
        # ★ إضافة (إصدار 8 — الميزة 5): مزامنة الجلسة — النافذة الرئيسية تمثل
        # المستخدم الحالي (نفس القيمة التي يضبطها تسجيل الدخول فلا سلوك جديد)
        CURRENT_USER["name"] = user_name
        # ★ إضافة (إصلاح 1 — الفحص الدوري): حالة نتيجة آخر فحص في الذاكرة
        # (لنافذة «عن البرنامج») + تذكر رقم إصدار الشريط المخفي بـ✕ + مؤقت
        # الفحص الدوري الصامت كل 30 دقيقة — يستدعي نفس دالة الفحص القائمة
        # في وضع الصمت التام: عند اكتشاف إصدار أحدث يظهر الشريط الأصفر
        # فوراً دون إعادة تشغيل، وبلا تحديث لا رسائل ولا أي أثر إطلاقاً
        self.update_last_check_result = None      # لم يُجرَ فحص بعد
        self.update_bar_dismissed_version = None  # رقم إصدار الشريط المخفي
        self._update_periodic_after_id = self.after(
            30 * 60 * 1000, self._update_periodic_check)
        # ★ إضافة (أرشيف الإصدارات): نقل ملفات main_backup_* القديمة بجوار
        # البرنامج إلى versions_archive عند بدء التشغيل مرة واحدة بصمت —
        # يُنظف مجلد البرنامج من فوضى الماضي (والنقل في سجل التدقيق)
        try:
            archive_migrate_old_backups()
        except Exception:
            pass
        self.style_ttk()
        self.build_sidebar()

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(side="left", fill="both", expand=True)

        # ★ الشريط العلوي للإحصائيات — يظهر في كل الشاشات
        self.build_stats_bar()

        self.pages = {}
        for name, builder in [("new", self.build_new_page), ("today", self.build_today_page),
                              ("archive", self.build_archive_page), ("search", self.build_search_page)]:
            pg = tk.Frame(self.container, bg=BG)
            self.pages[name] = pg
            builder(pg)

        # ★ إضافة (ميزة 6): تسجيل صفحة الفاتورة متعددة الأصناف
        pg = tk.Frame(self.container, bg=BG)
        self.pages["invoice"] = pg
        self.build_invoice_page(pg)
        # ★ تعديل ضروري معلن (إصدار 4 — ميزة 1): صفحات المدير تُبنى دائماً
        # (يبقى الدخول إليها محروساً بصلاحية المدير، وتُخفى أزرارها عن البائع
        # من الشريط الجانبي) — حتى يعمل «تبديل المستخدم» دون إعادة بناء الواجهة
        # ★ إضافة (ميزة 2): صفحة سجل التدقيق
        pg = tk.Frame(self.container, bg=BG)
        self.pages["audit"] = pg
        self.build_audit_page(pg)
        # ★ إضافة (إصدار 3 — ميزة 5+6): صفحتا إدارة المستخدمين وتقرير أداء البائعين
        pg = tk.Frame(self.container, bg=BG)
        self.pages["users"] = pg
        self.build_users_page(pg)
        pg = tk.Frame(self.container, bg=BG)
        self.pages["sellers"] = pg
        self.build_sellers_page(pg)
        # ★ إضافة (إصدار 4 — ميزة 2): صفحة لوحة المعلومات — للمدير فقط
        pg = tk.Frame(self.container, bg=BG)
        self.pages["dash"] = pg
        self.build_dashboard_page(pg)
        # ★ إضافة (إصدار 6): صفحة إعدادات الطباعة — تُبنى دائماً والدخول
        # إليها محروس بصلاحية المدير (زرها يُخفى عن البائع من الشريط الجانبي)
        pg = tk.Frame(self.container, bg=BG)
        self.pages["print"] = pg
        self.build_print_settings_page(pg)
        # ★ إضافة (إصدار 7 — الطبقة 4): صفحة النسخ والاستعادة — تُبنى دائماً
        # والدخول إليها محروس بصلاحية المدير (زرها يُخفى عن البائع من الشريط
        # الجانبي) — بنفس نهج صفحة إعدادات الطباعة في الإصدار 6
        pg = tk.Frame(self.container, bg=BG)
        self.pages["backups"] = pg
        self.build_backups_page(pg)

        # ★ إضافة (إصدار 4 — ميزة 5): تلميحات عربية على كل الأزرار
        self.attach_button_tips()

        # ★ إضافة (إصدار 8 — الميزة 5+6): بناء ظهور أزرار الشريط الجانبي حسب
        # صلاحيات المستخدم الفعلية + عناوين المجموعات الفاصلة (العمليات /
        # التقارير / الإدارة) — نفس الأزرار ونفس دوالها، تنظيم بصري فقط
        self.refresh_sidebar_permissions()

        self.show_page("new")
        self.protocol("WM_DELETE_WINDOW", self.exit_app)

        # ★ ملاحظات بدء التشغيل (ترقية قاعدة / حجر صحي) تُعرض مرة واحدة
        if NOTES:
            messagebox.showinfo("ملاحظات بدء التشغيل", "\n\n".join(NOTES))
            NOTES.clear()

    def report_callback_exception(self, exc, val, tb):
        """★ أي خطأ داخل زر/حدث: صندوق عربي + تسجيل، بدون إغلاق البرنامج"""
        log_error(val, tb)
        messagebox.showerror("خطأ غير متوقع",
            "حدث خطأ وتم تسجيله في error_log.txt — البرنامج لم يُغلق.\n\n"
            f"{getattr(exc, '__name__', type(val).__name__)}: {val}")

    # ---------- أدوات مساعدة ----------
    def style_ttk(self):
        st = ttk.Style(self)
        st.theme_use("clam")
        st.configure("Treeview", font=("Segoe UI", 10), rowheight=30,
                     background="white", fieldbackground="white", borderwidth=0)
        st.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"),
                     background="#dbe3ee", foreground=DARK, relief="flat")
        st.map("Treeview", background=[("selected", "#c7dbff")], foreground=[("selected", DARK)])

    def mk_btn(self, parent, text, cmd, color=ACCENT):
        return tk.Button(parent, text=text, command=cmd, bg=color, fg="white",
                         activebackground=color, activeforeground="white",
                         font=FB, bd=0, cursor="hand2", padx=16, pady=8, highlightthickness=0)

    def mk_card(self, parent, title, color):
        fr = tk.Frame(parent, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        tk.Label(fr, text=title, bg=CARD, fg=GRAY, font=("Segoe UI", 10)).pack(pady=(10, 0))
        v = tk.Label(fr, text="0", bg=CARD, fg=color, font=FV)
        v.pack(pady=(2, 10))
        return fr, v

    def mk_tree(self, parent, cols, widths):
        frm = tk.Frame(parent, bg="white", highlightbackground=BORDER, highlightthickness=1)
        tv = ttk.Treeview(frm, columns=cols, show="headings")
        vsb = ttk.Scrollbar(frm, orient="vertical", command=tv.yview)
        tv.configure(yscrollcommand=vsb.set)
        tv.pack(side="right", fill="both", expand=True)
        vsb.pack(side="left", fill="y")
        for c, w in zip(cols, widths):
            tv.heading(c, text=c)
            tv.column(c, width=w, anchor="center")
        return frm, tv

    def page_head(self, parent, title, subtitle=""):
        head = tk.Frame(parent, bg=BG)
        head.pack(fill="x", padx=25, pady=(18, 8))
        right = tk.Frame(head, bg=BG); right.pack(side="right")
        tk.Label(right, text=title, bg=BG, fg=DARK, font=FT).pack(anchor="e")
        if subtitle:
            tk.Label(right, text=subtitle, bg=BG, fg=GRAY, font=("Segoe UI", 10)).pack(anchor="e")
        return head

    # ★ إضافة (إصدار 8 — الميزة 5+6): خريطة صلاحيات أزرار الشريط الجانبي —
    # None تعني زراً متاحاً لكل المستخدمين (ليس له صلاحية في قائمة العشر)،
    # و«manager» تعني للمدير فقط — الأزرار تُبنى حسب الصلاحيات الفعلية
    NAV_PERMS = {
        "new": "add_ops", "invoice": "add_ops",
        "today": None, "archive": None, "search": None,
        "dash": "dashboard", "sellers": "perf_report",
        "users": "manager", "audit": "view_audit",
        "backups": "backup", "print": "print_settings",
        "update": "manager",   # ★ إضافة (إصدار 10): زر «التحديث» — للمدير فقط
    }
    # ★ إضافة (إصدار 8 — الميزة 6): مجموعات الشريط الجانبي بترتيبها الجديد —
    # نفس الأزرار الموجودة ونفس دوالها تماماً، تنظيم بصري فقط بعناوين فاصلة
    SIDEBAR_GROUPS = [
        ("العمليات", ["new", "invoice"]),
        ("التقارير", ["today", "archive", "search", "dash", "sellers"]),
        # ★ تعديل ضروري معلن (إصدار 10): إضافة زر التحديث لمجموعة «الإدارة»
        # كي يظهر تحت عنوانها ويُخفى عن البائع مع بقية أزرارها — كلمة واحدة
        # أُضيفت للقائمة ولم يتغير أي شيء آخر في التنظيم
        ("الإدارة",  ["users", "audit", "backups", "print", "update"]),
    ]

    # ---------- الشريط الجانبي ----------
    def build_sidebar(self):
        sb = tk.Frame(self, bg=SIDEBAR, width=220)
        sb.pack(side="right", fill="y"); sb.pack_propagate(False)
        tk.Label(sb, text="🖥️", bg=SIDEBAR, fg="white", font=("Segoe UI", 30)).pack(pady=(28, 0))
        tk.Label(sb, text="نظام المبيعات", bg=SIDEBAR, fg="white", font=FT).pack()
        tk.Label(sb, text="والمُرتجعات", bg=SIDEBAR, fg="#94a3b8", font=F).pack(pady=(0, 8))
        # ★ إضافة (إصدار 3 — ميزة 7): اسم المستخدم الحالي ودوره تحت الشعار
        # ★ تعديل ضروري معلن (إصدار 4 — ميزة 1): حفظ مرجع اللافتة لتحديث الاسم بعد تبديل المستخدم
        self.lbl_user = tk.Label(sb, text=f"👤 {self.user_name} ({self.role})", bg=SIDEBAR,
                                 fg="#93c5fd", font=("Segoe UI", 10, "bold"))
        self.lbl_user.pack(pady=(0, 14))

        self.nav_buttons = {}
        for key, label in [("new", "➕  عملية جديدة"), ("today", "📋  عمليات اليوم"),
                           ("archive", "🗂️  الأرشيف والتقارير"), ("search", "🔎  بحث")]:
            b = tk.Button(sb, text=label, font=FB, bd=0, cursor="hand2", anchor="e",
                          bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=lambda k=key: self.show_page(k))
            b.pack(fill="x", padx=10, pady=3)
            self.nav_buttons[key] = b

        # ★ إضافة (ميزة 6): زر شاشة الفاتورة متعددة الأصناف — بنفس نمط أزرار التنقل
        b_inv = tk.Button(sb, text="🧾  فاتورة أصناف", font=FB, bd=0, cursor="hand2", anchor="e",
                          bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.show_invoice)
        b_inv.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["invoice"] = b_inv

        # ★ تعديل ضروري معلن (إصدار 4 — ميزة 1): أزرار المدير تُنشأ دائماً وتُخفى
        # للبائع — لتصبح قابلة للإظهار/الإخفاء عند تبديل المستخدم دون إعادة البناء
        # ★ إضافة (إصدار 4 — ميزة 2): زر لوحة المعلومات — للمدير فقط
        b_dash = tk.Button(sb, text="📊  لوحة المعلومات", font=FB, bd=0, cursor="hand2", anchor="e",
                           bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                           activeforeground="white", padx=18, pady=11, highlightthickness=0,
                           command=self.show_dashboard)
        b_dash.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["dash"] = b_dash
        # ★ إضافة (ميزة 2): زر سجل التدقيق — للمدير فقط
        b_aud = tk.Button(sb, text="📜  سجل التدقيق", font=FB, bd=0, cursor="hand2", anchor="e",
                          bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.show_audit)
        b_aud.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["audit"] = b_aud
        # ★ إضافة (إصدار 3 — ميزة 5): زر إدارة المستخدمين — للمدير فقط
        b_usr = tk.Button(sb, text="👥  إدارة المستخدمين", font=FB, bd=0, cursor="hand2", anchor="e",
                          bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.show_users)
        b_usr.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["users"] = b_usr
        # ★ إضافة (إصدار 3 — ميزة 6): زر تقرير أداء البائعين — للمدير فقط
        b_rep = tk.Button(sb, text="📈  تقرير أداء البائعين", font=FB, bd=0, cursor="hand2", anchor="e",
                          bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.show_sellers)
        b_rep.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["sellers"] = b_rep
        # ★ إضافة (إصدار 4 — ميزة 1): قائمة أزرار المدير (تُخفى عن البائع وتظهر للمدير)
        self.manager_btns = [b_dash, b_aud, b_usr, b_rep]
        if self.role != "مدير":
            for b in self.manager_btns:
                b.pack_forget()

        # ★ إضافة (إصدار 6): زر إعدادات الطباعة — للمدير فقط، بنفس نمط أزرار
        # الشريط الجانبي، ويُضاف لقائمة أزرار المدير كي يُخفى عن البائع ويُعاد
        # إظهاره تلقائياً عند تبديل المستخدم (سطر القائمة نفسه لم يُمس)
        b_prn = tk.Button(sb, text="⚙️  إعدادات الطباعة", font=FB, bd=0, cursor="hand2",
                          anchor="e", bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.show_print_settings)
        b_prn.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["print"] = b_prn
        self.manager_btns.append(b_prn)
        add_tip(b_prn, "اختيار الطابعة الحرارية واسم المحل والطباعة التجريبية — للمدير فقط")
        if self.role != "مدير":
            b_prn.pack_forget()

        # ★ إضافة (إصدار 7 — الطبقة 4): زر النسخ والاستعادة — للمدير فقط،
        # بنفس نمط أزرار الشريط الجانبي، ويُضاف لقائمة أزرار المدير كي يُخفى
        # عن البائع ويُعاد إظهاره تلقائياً عند تبديل المستخدم
        b_bkp = tk.Button(sb, text="🗄️  النسخ والاستعادة", font=FB, bd=0, cursor="hand2",
                          anchor="e", bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.show_backups)
        b_bkp.pack(fill="x", padx=10, pady=3)
        self.nav_buttons["backups"] = b_bkp
        self.manager_btns.append(b_bkp)
        add_tip(b_bkp, "النسخ اليومية والشهرية والفورية واستعادة أي نسخة بأمان — للمدير فقط")
        if self.role != "مدير":
            b_bkp.pack_forget()

        # ★ إضافة (إصدار 10 — نظام التحديث التلقائي): زر «التحديث» — للمدير
        # فقط، بنفس نمط أزرار الشريط الجانبي، ويُضاف لقائمة أزرار المدير
        # وقائمة الصلاحيات (NAV_PERMS: "manager") كي يُخفى عن البائع ويُعاد
        # إظهاره تلقائياً عند تبديل المستخدم كإخوته في مجموعة الإدارة
        # ★ إصلاح (11 — البند ب): الزر يُخفى صراحة (pack_forget) عند بدء
        # التشغيل ولا يُحزم — لا يظهر إلا من داخل نتيجة مقارنة ناجحة تثبت
        # وجود إصدار أحدث من VERSION المحلي فعلياً (يُديره refresh_update_bar
        # وشرطه في refresh_sidebar_permissions — لا مصدر آخر لإظهاره)
        b_upd = tk.Button(sb, text="⬇️  التحديث", font=FB, bd=0, cursor="hand2",
                          anchor="e", bg=SIDEBAR, fg="#cbd5e1", activebackground=ACCENT,
                          activeforeground="white", padx=18, pady=11, highlightthickness=0,
                          command=self.update_now_dialog)
        b_upd.pack_forget()          # مخفي افتراضياً للجميع حتى تثبت المقارنة
        self.nav_buttons["update"] = b_upd
        self.manager_btns.append(b_upd)
        add_tip(b_upd, "فحص تحديثات البرنامج وتثبيتها — يظهر فقط عند توفر تحديث فعلي")

        self.mk_btn(sb, "⏻  خروج", self.exit_app, RED).pack(fill="x", padx=10, side="bottom", pady=(3, 20))
        # ★ إضافة (إصدار 4 — ميزة 1): زر «تبديل المستخدم» — لكل المستخدمين، فوق زر
        # «خروج» مباشرة (زر «خروج» نفسه يبقى كما هو تماماً — يغلق البرنامج كاملاً)
        self.mk_btn(sb, "🔄 تبديل المستخدم", self.switch_user, "#0369a1").pack(
            fill="x", padx=10, side="bottom", pady=3)
        self.mk_btn(sb, "💾 نسخة احتياطية الآن", self.backup_now, "#475569").pack(fill="x", padx=10, side="bottom", pady=3)
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 7): تغيير كلمة المرور أصبح لأي مستخدم
        # (كل مستخدم يغيّر كلمة مروره هو — وإعادة تعيين كلمات البائعين من شاشة إدارة المستخدمين)
        self.mk_btn(sb, "🔑 تغيير كلمة المرور", self.change_password_dialog,
                    "#7c3aed").pack(fill="x", padx=10, side="bottom", pady=3)

        # ★ إضافة (إصدار 8 — الميزة 7): قائمة المستخدم — زر واحد كبير أسفل
        # الشريط يفتح قائمة منسدلة تجمع إعداداته. الأزرار الأربعة القديمة أسفل
        # الشريط (تغيير كلمة المرور / نسخة احتياطية الآن / تبديل المستخدم /
        # خروج) بقيت كما هي بوظائفها تماماً — تُخفى من الشريط فقط ويُفتح بديل
        # عنها من القائمة المنسدلة (تعديل ضروري محدود في تخطيط الشريط فقط
        # صرّحت به المواصفة: نفس الدوال دون أي تغيير)
        self.bottom_action_btns = [w for w in sb.winfo_children()
                                   if isinstance(w, tk.Button) and w.cget("text") in
                                   ("🔑 تغيير كلمة المرور", "💾 نسخة احتياطية الآن",
                                    "🔄 تبديل المستخدم", "⏻  خروج")]
        for w in self.bottom_action_btns:
            w.pack_forget()
        self.btn_user_menu = tk.Button(
            sb, text=f"👤 {self.user_name} ({self.role})", font=FB, bd=0, cursor="hand2",
            anchor="e", bg="#0f172a", fg="#93c5fd", activebackground=ACCENT,
            activeforeground="white", padx=16, pady=10, highlightthickness=1,
            highlightbackground="#334155", command=self.show_user_menu)
        self.btn_user_menu.pack(fill="x", padx=10, side="bottom", pady=(3, 20))
        add_tip(self.btn_user_menu,
                "قائمة حسابك: 🔑 تغيير كلمة المرور • 💾 نسخة احتياطية الآن • "
                "🔄 تبديل المستخدم • ⏻ خروج")

    def refresh_sidebar_permissions(self):
        """★ إضافة (إصدار 8 — الميزة 5+6): بناء ظهور أزرار الشريط الجانبي حسب
        صلاحيات المستخدم الفعلية عند كل دخول/تبديل — الأزرار نفسها الموجودة
        (لا يُنشأ زر جديد ولا تُمس أي دالة) يُعاد ترتيبها داخل مجموعاتها مع
        عناوين فاصلة صغيرة، والعنوان يظهر فقط إن كان في مجموعته زر ظاهر"""
        sb = self.nav_buttons["new"].master      # إطار الشريط الجانبي نفسه
        # إزالة عناوين المجموعات القديمة (عناوين فقط — الأزرار لا تُمس)
        for h in getattr(self, "group_headers", {}).values():
            try:
                h.destroy()
            except Exception:
                pass
        self.group_headers = {}
        # كل زر يظهر حسب صلاحيته الفعلية ويُرتب داخل مجموعته (المدير: الكل)
        # (pack وحده لا ينقل زراً محزوماً مسبقاً — لا بد من فكه ثم إعادة حزمه)
        # ★ إصلاح (11 — البند ب): زر «التحديث» استثناء صارم — لا تكفي صلاحية
        # المدير وحدها لإظهاره؛ يظهر فقط إذا أثبت فحص ناجح وجود إصدار أحدث
        # فعلياً (update_available_version) — وإلا يُخفى كأي زر بلا صلاحية
        for gtitle, keys in self.SIDEBAR_GROUPS:
            first_visible = None
            for key in keys:
                b = self.nav_buttons[key]
                perm = self.NAV_PERMS.get(key)
                ok = perm is None or self.has_permission(perm)
                if key == "update":
                    ok = ok and bool(getattr(self, "update_available_version", None))
                if ok:
                    b.pack_forget()
                    b.pack(fill="x", padx=10, pady=3)
                    if first_visible is None:
                        first_visible = b
                else:
                    b.pack_forget()
            if first_visible is not None:        # العنوان يظهر فقط إن وُجد زر ظاهر
                h = tk.Label(sb, text=f"──  {gtitle}  ──", bg=SIDEBAR, fg="#64748b",
                             font=("Segoe UI", 8, "bold"))
                h.pack(fill="x", padx=14, before=first_visible)
                self.group_headers[gtitle] = h
        # تحديث نص زر قائمة المستخدم بعد أي دخول/تبديل
        if getattr(self, "btn_user_menu", None) is not None:
            self.btn_user_menu.config(text=f"👤 {self.user_name} ({self.role})")

    def show_user_menu(self):
        """★ إضافة (إصدار 8 — الميزة 7): قائمة المستخدم المنسدلة — تجمع إعداداته
        في مكان واحد، وتنفذ نفس الدوال الأربع الموجودة تماماً دون أي تغيير فيها"""
        m = tk.Menu(self, tearoff=0, bg=CARD, fg=DARK, font=("Segoe UI", 10),
                    activebackground=ACCENT, activeforeground="white", bd=0, relief="flat")
        m.add_command(label="🔑 تغيير كلمة المرور", command=self.change_password_dialog)
        m.add_command(label="💾 نسخة احتياطية الآن", command=self.backup_now)
        m.add_command(label="🔄 تبديل المستخدم", command=self.switch_user)
        m.add_separator()
        # ★ إضافة (إصلاح 2): مدخل دائم واضح لنافذة «عن البرنامج» لكل
        # المستخدمين من قائمة المستخدم — قراءة فقط بلا أي اتصال شبكي
        m.add_command(label="ℹ️ عن البرنامج", command=self.about_dialog)
        # ★ إضافة (إصلاح 3 — البند ب): «فحص التحديثات الآن» دائم الظهور
        # للمدير — فحص فوري برسالة نتيجة عربية دائماً (وللشريط الأصفر زره
        # الخاص بجانب «تحديث الآن")
        if self.role == "مدير":
            m.add_command(label="🔄 فحص التحديثات الآن",
                          command=lambda: self.update_check_manual(None))
            # ★ إضافة (أرشيف الإصدارات): عرض أرشيف الإصدارات — للمدير فقط
            m.add_command(label="🗃️ أرشيف الإصدارات",
                          command=self.archive_versions_dialog)
        m.add_separator()
        m.add_command(label="⏻ خروج (إغلاق البرنامج)", command=self.exit_app)
        try:
            x = self.btn_user_menu.winfo_rootx()
            y = self.btn_user_menu.winfo_rooty() + self.btn_user_menu.winfo_height()
            m.tk_popup(x, y)
        finally:
            m.grab_release()

    # ---------- ★ الشريط العلوي ----------
    def build_stats_bar(self):
        bar = tk.Frame(self.container, bg=BG)
        bar.pack(fill="x", padx=25, pady=(15, 5))
        # ★ إضافة (إصدار 10): حفظ مرجع الشريط الإحصائي كي يوضع شريط إشعار
        # التحديث الأصفر فوقه مباشرة (before=) دون أي تغيير آخر في البناء
        self.stats_bar_frame = bar
        self.stats_widgets = {}
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): الشريط العلوي 5 بطاقات —
        # عدد العمليات (رمادي) / نقداً (أخضر) / شبكة (أزرق) / المرتجعات (أحمر) /
        # الإجمالي (أزرق) — لفصل مبيعات الدرج النقدي عن مبيعات جهاز الشبكة
        for title, color in [("عدد العمليات", "#334155"), ("نقداً", GREEN),
                             ("شبكة", ACCENT), ("المرتجعات", RED),
                             ("الإجمالي", "#1d4ed8")]:
            fr, val = self.mk_card(bar, title, color)
            fr.pack(side="right", expand=True, fill="x", padx=5)
            self.stats_widgets[title] = val
        self.refresh_stats()

    def refresh_stats(self):
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): day_totals ترجع الآن
        # (عدد العمليات، نقداً، شبكة، المرتجعات، الإجمالي)
        n, cash, netw, rets, net = day_totals(today_str())
        self.stats_widgets["عدد العمليات"].config(text=str(n))
        self.stats_widgets["نقداً"].config(text=money(cash))
        self.stats_widgets["شبكة"].config(text=money(netw))
        self.stats_widgets["المرتجعات"].config(text=money(rets))
        self.stats_widgets["الإجمالي"].config(text=money(net),
                                               fg=(GREEN if net >= 0 else RED))

    def show_page(self, key):
        for k, b in self.nav_buttons.items():
            b.config(bg=(ACCENT if k == key else SIDEBAR), fg=("white" if k == key else "#cbd5e1"))
        for pg in self.pages.values():
            pg.pack_forget()
        self.pages[key].pack(fill="both", expand=True)
        self.refresh_stats()   # ★ تحديث الشريط عند كل تنقل
        if key == "new":
            self.refresh_items(); self.update_closed_banner()
        elif key == "today":
            self.refresh_today()
        elif key == "archive":
            self.refresh_archive()

    # ---------- صفحة عملية جديدة ----------
    def build_new_page(self, p):
        self.page_head(p, "➕ عملية جديدة", f"تاريخ اليوم: {today_str()}  ({day_name(today_str())})")
        self.banner_closed = tk.Label(p, text="", bg=BG, fg=RED, font=FB, wraplength=900)
        self.banner_closed.pack(fill="x", padx=25)

        form = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        form.pack(fill="x", padx=25, pady=10)

        def field_row(label):
            fr = tk.Frame(form, bg=CARD); fr.pack(fill="x", padx=22, pady=6)
            tk.Label(fr, text=label, bg=CARD, fg=DARK, font=FB, width=11, anchor="e").pack(side="right")
            inner = tk.Frame(fr, bg=CARD)
            inner.pack(side="right", padx=(0, 10))
            return inner

        in1 = field_row("اسم الصنف:")
        self.cb_item = ttk.Combobox(in1, font=F, width=30)
        self.cb_item.pack(side="right", ipady=4)

        in2 = field_row("الكمية:")
        self.e_qty = tk.Entry(in2, font=F, justify="center", relief="solid", bd=1, width=30)
        self.e_qty.pack(side="right", ipady=4)

        in3 = field_row("السعر:")
        self.e_price = tk.Entry(in3, font=F, justify="center", relief="solid", bd=1, width=30)
        self.e_price.pack(side="right", ipady=4)

        # ★ إضافة (ميزة 5): صف اسم العميل الاختياري — يُخزن مع العملية
        in_c = field_row("اسم العميل:")
        self.e_customer = tk.Entry(in_c, font=F, justify="center", relief="solid", bd=1, width=30)
        self.e_customer.pack(side="right", ipady=4)
        tk.Label(in_c, text="(اختياري)", bg=CARD, fg=GRAY,
                 font=("Segoe UI", 9)).pack(side="right", padx=(6, 0))

        trow = tk.Frame(form, bg=CARD); trow.pack(fill="x", padx=22, pady=8)
        tk.Label(trow, text="النوع:", bg=CARD, fg=DARK, font=FB).pack(side="right")
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): ثلاثة أنواع — نقداً (أخضر:
        # الدرج النقدي) وشبكة (أزرق: جهاز الشبكة) بقيمة موجبة عادية،
        # ومرتجع (أحمر) بقيمة سالبة كما هو الآن
        self.type_var = tk.StringVar(value="نقداً")
        for txt, col in [("نقداً", GREEN), ("شبكة", ACCENT), ("مرتجع", RED)]:
            tk.Radiobutton(trow, text=txt, variable=self.type_var, value=txt, font=FB,
                           fg=col, bg=CARD, selectcolor="#dbeafe", activebackground=CARD,
                           activeforeground=col, indicatoron=0, width=10, bd=1,
                           relief="solid", cursor="hand2", command=self.update_calc).pack(side="right", padx=10)

        crow = tk.Frame(form, bg="#f8fafc"); crow.pack(fill="x", padx=22, pady=(4, 10))
        fr = tk.Frame(crow, bg="#f8fafc"); fr.pack(expand=True, fill="x")
        tk.Label(fr, text="المبيع (الكمية × السعر)", bg="#f8fafc", fg=GRAY, font=("Segoe UI", 10)).pack()
        self.lbl_total_v = tk.Label(fr, text="—", bg="#f8fafc", fg=DARK, font=FV)
        self.lbl_total_v.pack()

        srow = tk.Frame(form, bg=CARD); srow.pack(fill="x", padx=22, pady=(2, 16))
        self.mk_btn(srow, "💾  حفظ العملية", self.save_op).pack(side="right")
        self.lbl_status = tk.Label(srow, text="", bg=CARD, font=FB)
        self.lbl_status.pack(side="right", padx=14)

        for e in (self.e_qty, self.e_price):
            e.bind("<KeyRelease>", self.update_calc)
            e.bind("<Return>", lambda e: self.save_op())
        self.cb_item.bind("<Return>", lambda e: self.save_op())

    def update_calc(self, *_):
        q, pr = to_num(self.e_qty.get()), to_num(self.e_price.get())
        if q is None or pr is None:
            self.lbl_total_v.config(text="—", fg=DARK); return
        total = q * pr
        if self.type_var.get() == "مرتجع":
            total = -total
        self.lbl_total_v.config(text=money(total), fg=(ACCENT if total >= 0 else RED))

    def save_op(self):
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «إضافة عمليات وفواتير» — الفحص
        # الدقيق الجديد (المدير يملك كل الصلاحيات دائماً ولا يلاحظ الفرق)
        if not self.has_permission("add_ops"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «إضافة عمليات وفواتير»")
            return
        d = today_str()
        if is_closed(d):
            messagebox.showwarning("اليوم مغلق",
                "تم إغلاق اليوم وحفظ تقريره.\nلا يمكن إضافة عمليات على يوم مغلق.\n"
                "➡ يمكنك إعادة فتح اليوم من شاشة الأرشيف.")
            return
        item = self.cb_item.get().strip()
        if not item:
            messagebox.showwarning("تنبيه", "اكتب اسم الصنف أولاً"); return
        q  = to_num(self.e_qty.get())
        pr = to_num(self.e_price.get())
        if q is None or q <= 0:
            messagebox.showwarning("تنبيه",
                f"الكمية غير صحيحة: «{self.e_qty.get()}»\nأدخل رقماً أكبر من صفر"); return
        if pr is None or pr < 0:
            messagebox.showwarning("تنبيه",
                f"السعر غير صحيح: «{self.e_price.get()}»\nأدخل رقماً صحيحاً"); return
        t = self.type_var.get()
        total = q * pr
        if t == "مرتجع":
            total = -total   # المرتجع بقيمة سالبة
        cust = self.e_customer.get().strip()   # ★ إضافة (ميزة 5): العميل الاختياري
        try:
            with connect() as conn:
                # ★ تعديل ضروري معلن (ميزة 5): أصبح الحفظ يشمل عمود customer_name
                # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): الحفظ يسجل اسم البائع تلقائياً
                conn.execute("INSERT INTO operations(date,item_name,quantity,price,total,type,customer_name,seller_name)"
                             " VALUES(?,?,?,?,?,?,?,?)",
                             (d, item, q, pr, total, t, cust, CURRENT_USER["name"]))
        except Exception as e:
            messagebox.showerror("خطأ في الحفظ", f"تعذر حفظ العملية:\n{e}")
            return
        for e in (self.e_qty, self.e_price):
            e.delete(0, "end")
        self.e_customer.delete(0, "end")       # ★ إضافة (ميزة 5): مسح حقل العميل بعد الحفظ
        self.type_var.set("نقداً"); self.update_calc()   # ★ تعديل (إصدار 5): عودة الاختيار تلقائياً إلى «نقداً» بعد الحفظ
        self.refresh_items(); self.refresh_today(); self.refresh_stats()
        self.lbl_status.config(text=f"✔ تم حفظ العملية ({t})", fg=GREEN)
        audit("حفظ عملية",                      # ★ إضافة (ميزة 2): تسجيل الحفظ في سجل التدقيق
              f"{t}: {item} — {q:g} × {pr:g} = {total:g}" + (f" | عميل: {cust}" if cust else ""))

    def refresh_items(self):
        with connect() as conn:
            vals = [r[0] for r in conn.execute("SELECT DISTINCT item_name FROM operations ORDER BY item_name")]
        self.cb_item["values"] = vals
        # ★ إضافة (ميزة 6): نفس قائمة الأصناف تتذكر لشاشة الفاتورة أيضاً
        if hasattr(self, "cb_inv_item"):
            self.cb_inv_item["values"] = vals

    def update_closed_banner(self):
        if is_closed(today_str()):
            self.banner_closed.config(text="⚠️ تم إغلاق اليوم وحفظ تقريره — لا يمكن إضافة عمليات. (يمكن إعادة الفتح من الأرشيف)")
        else:
            self.banner_closed.config(text="")

    # ---------- صفحة عمليات اليوم ----------
    def build_today_page(self, p):
        head = self.page_head(p, "📋 عمليات اليوم", "الإحصائيات ظاهرة في الشريط العلوي ↑")
        self.mk_btn(head, "🔄 تحديث", self.refresh_today, "#475569").pack(side="left", pady=6)

        # ★ إضافة (إصدار 4 — ميزة 4): فلتر النوع بجانب زر التحديث —
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): أصبح (الكل/نقداً/شبكة/مرتجع) —
        # فلترة عرض الجدول فقط، يتكامل مع فلتر البائع (البائع + النوع معاً)،
        # واختيار «مرتجع» يعرض الصفوف بالأحمر كما هي موجودة
        self.fr_today_type = tk.Frame(head, bg=BG)
        self.fr_today_type.pack(side="left", padx=(12, 0))
        self.today_type_var = tk.StringVar(value="الكل")
        for txt, col, tip in [("الكل", DARK, "عرض كل العمليات"),
                              ("نقداً", GREEN, "عرض عمليات الدرج النقدي فقط"),
                              ("شبكة", ACCENT, "عرض عمليات جهاز الشبكة فقط"),
                              ("مرتجع", RED, "عرض عمليات المرتجع فقط")]:
            rb = tk.Radiobutton(self.fr_today_type, text=txt, variable=self.today_type_var,
                                value=txt, font=FB, fg=col, bg=BG, selectcolor="#dbeafe",
                                activebackground=BG, activeforeground=col, indicatoron=0,
                                width=7, bd=1, relief="solid", cursor="hand2",
                                command=self.refresh_today)
            rb.pack(side="right", padx=3)
            add_tip(rb, tip)          # ★ (إصدار 4 — ميزة 5): تلميح الفلتر

        # ★ تعديل ضروري معلن (إصدار 4 — ميزة 1): ملاحظة البائع وفلتر البائع يُنشآن
        # دائماً ويُظهر أحدهما حسب الدور — لتتكيف الشاشة عند تبديل المستخدم دون إعادة بنائها
        # ★ إضافة (إصدار 3 — ميزة 4): البائع يرى عملياته فقط — والمدير يفلتر حسب البائع
        self.lbl_today_only = tk.Label(head, text="تُعرض عملياتك فقط", bg=BG, fg=GRAY,
                                       font=("Segoe UI", 10, "bold"))
        self.fr_today_filter = ffr = tk.Frame(head, bg=BG)
        tk.Label(ffr, text="البائع:", bg=BG, fg=DARK, font=FB).pack(side="right")
        self.cb_today_filter = ttk.Combobox(ffr, font=F, width=14, state="readonly",
                                            values=["الكل"])
        self.cb_today_filter.current(0)
        self.cb_today_filter.pack(side="right", padx=(0, 6))
        self.cb_today_filter.bind("<<ComboboxSelected>>", lambda e: self.refresh_today())
        if self.role != "مدير":
            self.lbl_today_only.pack(side="left", padx=12)
        else:
            ffr.pack(side="left", padx=12)

        self.lbl_closed = tk.Label(p, text="", bg=BG, fg=GREEN, font=FB)
        self.lbl_closed.pack(fill="x", padx=25)

        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): عمود البائع في جدول عمليات اليوم
        frm, self.tv_today = self.mk_tree(p,
            ["النوع", "المبيع", "السعر", "الكمية", "اسم الصنف", "العميل", "البائع", "التاريخ"],
            [80, 110, 100, 80, 190, 140, 100, 100])
        frm.pack(fill="both", expand=True, padx=25, pady=8)
        self.tv_today.tag_configure("ret", foreground=RED)

        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25, pady=(0, 18))
        self.mk_btn(bar, "🗑 حذف العملية المحددة", self.delete_selected, RED).pack(side="right", padx=6)
        self.btn_close = self.mk_btn(bar, "🔒 إغلاق اليوم وحفظ التقرير", self.close_day, ORANGE)
        self.btn_close.pack(side="left", padx=6)

    def refresh_today(self):
        d = today_str()
        self.tv_today.delete(*self.tv_today.get_children())
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 4): البائع يرى عملياته فقط،
        # والمدير يرى الكل أو بائعاً محدداً من القائمة المنسدلة
        q = "SELECT * FROM operations WHERE date=?"
        params = [d]
        # ★ تعديل ضروري معلن (إصدار 4 — ميزة 4): احترام فلتر النوع
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): القيم (الكل/نقداً/شبكة/مرتجع) —
        # فلترة عرض الجدول فقط (البطاقات والشريط العلوي كما هما)، ويتكامل مع فلتر البائع
        if getattr(self, "today_type_var", None) is not None and \
                self.today_type_var.get() not in ("الكل", ""):
            q += " AND type=?"
            params.append(self.today_type_var.get())
        if self.role != "مدير":
            q += " AND seller_name=?"
            params.append(self.user_name)
        elif hasattr(self, "cb_today_filter"):
            flt = self.cb_today_filter.get()
            if flt not in ("الكل", ""):
                q += " AND seller_name=?"
                params.append("" if flt == "غير محدد" else flt)
        q += " ORDER BY id DESC"
        with connect() as conn:
            rows = conn.execute(q, params).fetchall()
        for r in rows:
            self.tv_today.insert("", "end", iid=str(r["id"]),
                tags=(("ret",) if r["type"] == "مرتجع" else ()),
                values=(r["type"], money(r["total"]), money(r["price"]),
                        f'{r["quantity"]:g}', r["item_name"],
                        (r["customer_name"] or ""),
                        (r["seller_name"] or "—"), r["date"]))   # ★ ميزة 3+5 (إصدار 3): عمودا العميل والبائع
        # ★ إضافة (إصدار 3 — ميزة 4): تحديث قائمة الفلترة بأسماء بائعي اليوم
        if self.role == "مدير" and hasattr(self, "cb_today_filter"):
            with connect() as conn:
                names = [r[0] or "غير محدد" for r in conn.execute(
                    "SELECT DISTINCT seller_name FROM operations WHERE date=? "
                    "ORDER BY seller_name", (d,))]
            self.cb_today_filter["values"] = ["الكل"] + names
        closed = is_closed(d)
        self.btn_close.config(state=("disabled" if closed else "normal"))
        self.lbl_closed.config(text=("🔒 تم إغلاق هذا اليوم وحفظ تقريره في الأرشيف" if closed else ""))

    def delete_selected(self):
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «حذف عملية» بدل «المدير فقط»
        if not self.require_admin("delete_op"):
            return
        sel = self.tv_today.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر عملية من الجدول أولاً"); return
        if is_closed(today_str()):
            messagebox.showwarning("اليوم مغلق", "لا يمكن الحذف — اليوم مغلق"); return
        if not messagebox.askyesno("تأكيد", "هل تريد حذف هذه العملية نهائياً؟"):
            return
        with connect() as conn:
            conn.execute("DELETE FROM operations WHERE id=?", (int(sel[0]),))
        audit("حذف عملية", f"رقم {sel[0]}")     # ★ إضافة (ميزة 2): تسجيل الحذف
        self.refresh_today(); self.refresh_stats()
        self.lbl_status.config(text="🗑 تم حذف العملية", fg=RED)

    def close_day(self):
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «إغلاق اليوم» بدل «المدير فقط»
        if not self.require_admin("close_day"):
            return
        d = today_str()
        if is_closed(d):
            messagebox.showinfo("مغلق", "تم إغلاق اليوم مسبقاً"); return
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): day_totals ترجع الآن
        # (عدد العمليات، نقداً، شبكة، المرتجعات، الإجمالي)
        n, cash, netw, rets, net = day_totals(d)
        if n == 0 and not messagebox.askyesno("تأكيد", "لا توجد عمليات اليوم.\nهل تريد إغلاق اليوم بتقرير فارغ؟"):
            return
        # ★ تعديل (إصدار 5): الملخص قبل الإغلاق يعرض نقداً وشبكة منفصلين
        # حتى يطابق المدير الدرج النقدي وكشف جهاز الشبكة قبل القفل
        msg = (f"ملخص يوم {d}:\n\nعدد العمليات: {n}\nنقداً: {money(cash)}\n"
               f"شبكة: {money(netw)}\nالمرتجعات: {money(rets)}\nالإجمالي: {money(net)}\n\n"
               "سيُحفظ التقرير في الأرشيف ولا يمكن إضافة عمليات على هذا اليوم.\n"
               "✔ تأكد من مطابقة الدرج النقدي وكشف جهاز الشبكة قبل المتابعة.\nهل تريد المتابعة؟")
        if not messagebox.askyesno("إغلاق اليوم", msg):
            return
        with connect() as conn:
            # ★ تعديل (إصدار 5): حفظ total_cash و total_network منفصلين
            # في تقرير اليوم مع total_sales = نقداً + شبكة
            conn.execute("""INSERT INTO daily_reports(report_date,ops_count,total_sales,
                            total_returns,net_total,total_cash,total_network,closed_at)
                            VALUES(?,?,?,?,?,?,?,?)""",
                         (d, n, cash + netw, rets, net, cash, netw,
                          datetime.now().strftime("%Y-%m-%d %H:%M")))
        audit("إغلاق يوم", f"{d}: {n} عملية — نقداً {money(cash)} | شبكة {money(netw)} | "
              f"مرتجعات {money(rets)} | إجمالي {money(net)}")
        # ★ إضافة (إصدار 7 — طبقات الحماية 1+2+3): النسخ الاحتياطي التلقائي
        # بعد حفظ الإغلاق مباشرة — نسخة يومية (آخر 30) + شهرية أول إغلاق في
        # الشهر (لا تُحذف أبداً) وتُنسخان إلى المجلد الخارجي إن كان مختاراً —
        # وفشل النسخ لا يلغي إغلاق اليوم أبداً: رسالة تحذير + تسجيل في
        # error_log فقط (كما تنص المواصفة تماماً)
        try:
            bk_errors = make_auto_backup(d)
            if bk_errors:
                log_error(RuntimeError("؛ ".join(bk_errors)))
                messagebox.showwarning("تحذير النسخ الاحتياطي",
                    "تم إغلاق اليوم وحفظ تقريره بنجاح ✅\nلكن تعذر إتمام النسخ الاحتياطي:\n"
                    "• " + "\n• ".join(bk_errors) +
                    "\n\nسُجل الخطأ في error_log.txt.")
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showwarning("تحذير النسخ الاحتياطي",
                "تم إغلاق اليوم وحفظ تقريره بنجاح ✅\n"
                "لكن فشل النسخ الاحتياطي التلقائي (سُجل في error_log.txt).")
        self.refresh_today(); self.update_closed_banner(); self.refresh_stats()
        if messagebox.askyesno("تم", "تم حفظ تقرير اليوم بنجاح ✅\nهل تريد عرض التقرير الآن؟"):
            self.open_day_details(d)
        # ★ إضافة (إصدار 6 — ربط الطباعة بالإغلاق): بعد حفظ تقرير اليوم بنجاح —
        # إن كانت الطباعة التلقائية مفعلة (auto_print_daily) تطبع مباشرة دون
        # سؤال، وإلا تُسأل «هل تريد طباعة تقرير اليوم؟» (بعد سؤال عرض التقرير
        # وليس بدله) — وفشل الطباعة لا يلغي حفظ اليوم أبداً لأن الحفظ حدث
        # قبلها بأمان، وأي خطأ يسجل في error_log دون أي انهيار
        try:
            if get_setting("auto_print_daily") == "1":
                self.print_day_report(d, closer=CURRENT_USER["name"], when="بعد الإغلاق")
            elif messagebox.askyesno("الطباعة", "هل تريد طباعة تقرير اليوم؟"):
                self.print_day_report(d, closer=CURRENT_USER["name"], when="بعد الإغلاق")
        except Exception as e:
            log_error(e, sys.exc_info()[2])

    # ---------- الأرشيف ----------
    def build_archive_page(self, p):
        head = self.page_head(p, "🗂️ الأرشيف والتقارير", "كل التقارير اليومية المحفوظة في قاعدة البيانات")
        self.mk_btn(head, "🔄 تحديث", self.refresh_archive, "#475569").pack(side="left", pady=6)

        # ★ إضافة (ميزة 4): بطاقة تصفية الأرشيف بمدى تاريخ — تقبل عدة صيغ للتاريخ
        frow = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        frow.pack(fill="x", padx=25, pady=6)
        def date_cell(label):
            c = tk.Frame(frow, bg=CARD); c.pack(side="right", padx=10, pady=10)
            tk.Label(c, text=label, bg=CARD, fg=DARK, font=FB).pack(side="right")
            e = tk.Entry(c, font=F, justify="center", relief="solid", bd=1, width=13)
            e.pack(side="right", padx=(6, 0), ipady=4)
            return e
        self.e_from = date_cell("من تاريخ:")
        self.e_to   = date_cell("إلى تاريخ:")
        tk.Label(frow, text="الصيغ المقبولة: 2025-01-10 أو 10-01-2025 أو 10/01/2025",
                 bg=CARD, fg=GRAY, font=("Segoe UI", 9)).pack(side="right", padx=10)
        self.mk_btn(frow, "🔍 تصفية", self.filter_archive, ACCENT).pack(side="left", padx=10)
        self.mk_btn(frow, "↩ عرض الكل", self.show_all_archive, "#475569").pack(side="left", padx=6)

        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): جدول الأرشيف يعرض
        # التاريخ | عدد العمليات | نقداً | شبكة | المرتجعات | الإجمالي | وقت الإغلاق
        frm, self.tv_arch = self.mk_tree(p,
            ["وقت الإغلاق", "الإجمالي", "المرتجعات", "شبكة", "نقداً", "عدد العمليات", "التاريخ"],
            [130, 110, 110, 105, 105, 95, 100])
        frm.pack(fill="both", expand=True, padx=25, pady=8)
        self.tv_arch.bind("<Double-1>", lambda e: self.open_selected_day())

        # ★ إضافة (ميزة 4): سطر الإجمالي التراكمي للأيام المعروضة
        self.lbl_arch_summary = tk.Label(p, text="", bg=BG, fg=ACCENT, font=FB)
        self.lbl_arch_summary.pack(fill="x", padx=25)

        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25, pady=(0, 18))
        self.mk_btn(bar, "🔓 إعادة فتح اليوم", self.reopen_day, "#7c3aed").pack(side="left", padx=6)
        # ★ إضافة (ميزة 3): زر تصدير الأرشيف كاملاً إلى Excel حقيقي
        self.mk_btn(bar, "📊 تصدير الأرشيف كاملاً Excel", self.export_archive_xlsx, "#0d9488").pack(side="right", padx=6)
        self.mk_btn(bar, "📥 تصدير اليوم إلى CSV", self.export_selected_day, GREEN).pack(side="right", padx=6)
        self.mk_btn(bar, "📄 عرض تفاصيل اليوم", self.open_selected_day).pack(side="right", padx=6)
        # ★ إضافة (إصدار 6): زر طباعة تقرير اليوم المحدد من شريط الأرشيف —
        # إعادة طباعة تقرير الإغلاق من بيانات daily_reports المحفوظة
        b_arch_prn = self.mk_btn(bar, "🖨 طباعة التقرير", self.print_selected_day, "#334155")
        b_arch_prn.pack(side="right", padx=6)
        add_tip(b_arch_prn, "طباعة تقرير اليوم المحدد على الطابعة الحرارية (إعادة طباعة)")
        # ★ إضافة (إصدار 7 — الميزة 8): زر «🖨 طباعة/معاينة A4» لتقرير اليوم
        # المحدد (بجانب زر الطباعة الحرارية الموجود) + زر «📄 تقرير الفترة A4»
        # للملخص الإجمالي بعد فلترة مدى التاريخ — كلاهما يفتح نافذة المعاينة
        # أولاً ولا طباعة مباشرة بدونها
        b_arch_a4 = self.mk_btn(bar, "🖨 طباعة/معاينة A4", self.print_selected_day_a4, "#1d4ed8")
        b_arch_a4.pack(side="right", padx=6)
        add_tip(b_arch_a4, "معاينة تقرير اليوم المحدد ثم طباعته على A4 عبر ملف PDF قياسي")
        b_arch_prd = self.mk_btn(bar, "📄 تقرير الفترة A4", self.print_period_report, "#0f766e")
        b_arch_prd.pack(side="right", padx=6)
        add_tip(b_arch_prd, "تقرير A4 دوري لكل الأيام ضمن مدى التاريخ المُصفّى أعلاه مع جدول الأيام والإجمالي التراكمي")

        # ★ إضافة (إصدار 8 — الميزة 4): دمج أزرار شريط الأرشيف كلها في زر
        # «⚙️ الإجراءات» واحد يفتح قائمة منسدلة — تعديل ضروري محدود في تخطيط
        # شريط الأرشيف فقط صرّحت به المواصفة: الأزرار الموجودة تُخفى من الشريط
        # وتُفتح كلها من القائمة بنفس الدوال ونفس المنطق تماماً
        self.arch_action_btns = [w for w in bar.winfo_children() if isinstance(w, tk.Button)]
        for w in self.arch_action_btns:
            w.pack_forget()
        self.arch_menu_btn = self.mk_btn(bar, "⚙️ الإجراءات", self.show_archive_menu, "#334155")
        self.arch_menu_btn.pack(side="right", padx=6)
        add_tip(self.arch_menu_btn,
                "كل إجراءات اليوم المحدد: عرض التفاصيل • طباعة/معاينة A4 • طباعة حرارية • "
                "تصدير CSV/Excel • تقرير الفترة A4 • إعادة فتح اليوم")
        tk.Label(bar, text="اختر اليوم من الجدول ثم اضغط زر الإجراءات",
                 bg=BG, fg=GRAY, font=("Segoe UI", 9)).pack(side="right", padx=8)
        self.refresh_archive()

    def refresh_archive(self):
        self.tv_arch.delete(*self.tv_arch.get_children())
        with connect() as conn:
            rows = conn.execute("SELECT * FROM daily_reports ORDER BY report_date DESC").fetchall()
        for r in rows:
            # ★ تعديل (إصدار 5): القيم تشمل نقداً وشبكة منفصلين
            self.tv_arch.insert("", "end", iid=r["report_date"], values=(
                r["closed_at"], money(r["net_total"]), money(r["total_returns"]),
                money(r["total_network"] or 0), money(r["total_cash"] or 0),
                r["ops_count"], r["report_date"]))
        self.update_arch_summary(rows)   # ★ إضافة (ميزة 4): تحديث الإجمالي التراكمي

    def open_selected_day(self):
        sel = self.tv_arch.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر يوماً من الجدول أولاً"); return
        self.open_day_details(sel[0])

    def open_day_details(self, d):
        with connect() as conn:
            rep = conn.execute("SELECT * FROM daily_reports WHERE report_date=?", (d,)).fetchone()
            # ★ تعديل ضروري معلن (إصدار 3 — ميزة 4): البائع يرى عملياته فقط في تفاصيل اليوم
            q = "SELECT * FROM operations WHERE date=?"
            params = [d]
            if self.role != "مدير":
                q += " AND seller_name=?"
                params.append(self.user_name)
            q += " ORDER BY id"
            rows = conn.execute(q, params).fetchall()
        if rep is None:
            return
        # ★ إضافة (إصدار 8 — الميزة 3): تسجيل النافذة في التتبع المركزي
        # (تُغلق تلقائياً عند تبديل المستخدم)
        win = self.register_window(tk.Toplevel(self))
        win.title(f"تقرير يوم {d}")
        win.geometry("1010x560"); win.configure(bg=BG)   # ★ (إصدار 3): توسعة بسيطة لاستيعاب عمود البائع
        tk.Label(win, text=f"📄 تقرير يوم {d}  ({day_name(d)})", bg=BG, fg=DARK, font=FT).pack(pady=12)
        # ★ إضافة (إصدار 3 — ميزة 4): ملاحظة للبائع أنه يرى عملياته فقط
        if self.role != "مدير":
            tk.Label(win, text="تُعرض عملياتك فقط", bg=BG, fg=GRAY,
                     font=("Segoe UI", 10, "bold")).pack()

        cards = tk.Frame(win, bg=BG); cards.pack(fill="x", padx=20)
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): بطاقات تفاصيل اليوم
        # تعرض نقداً وشبكة منفصلين — الترقية عبّأت التقارير القديمة تلقائياً
        # (total_cash = total_sales و total_network = 0)
        for title, val, color in [("العمليات", rep["ops_count"], "#334155"),
                                  ("نقداً", money(rep["total_cash"] or 0), GREEN),
                                  ("شبكة", money(rep["total_network"] or 0), ACCENT),
                                  ("المرتجعات", money(rep["total_returns"]), RED),
                                  ("الإجمالي", money(rep["net_total"]),
                                   GREEN if rep["net_total"] >= 0 else RED)]:
            fr, v = self.mk_card(cards, title, color)
            fr.pack(side="right", expand=True, fill="x", padx=4)
            v.config(text=str(val))

        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): عمود البائع في تفاصيل الأرشيف
        frm, tv = self.mk_tree(win,
            ["النوع", "المبيع", "السعر", "الكمية", "اسم الصنف", "العميل", "البائع", "التاريخ"],
            [80, 110, 100, 80, 190, 130, 100, 100])
        frm.pack(fill="both", expand=True, padx=20, pady=10)
        tv.tag_configure("ret", foreground=RED)
        for r in rows:
            tv.insert("", "end", tags=(("ret",) if r["type"] == "مرتجع" else ()),
                values=(r["type"], money(r["total"]), money(r["price"]),
                        f'{r["quantity"]:g}', r["item_name"],
                        (r["customer_name"] or ""),
                        (r["seller_name"] or "—"), r["date"]))   # ★ ميزة 3+5 (إصدار 3): عمودا العميل والبائع

        bar = tk.Frame(win, bg=BG); bar.pack(pady=(0, 15))
        self.mk_btn(bar, "📥 تصدير CSV", lambda: self.export_ops_csv(d, rows, rep), GREEN).pack(side="right", padx=6)
        # ★ إضافة (ميزة 3): زر تصدير هذا اليوم إلى Excel حقيقي
        self.mk_btn(bar, "📊 تصدير Excel", lambda: self.export_day_xlsx(d, rows, rep), "#0d9488").pack(side="right", padx=6)
        # ★ إضافة (إصدار 6): زر طباعة تقرير هذا اليوم على الطابعة الحرارية —
        # إعادة طباعة تقرير الإغلاق من بيانات daily_reports المحفوظة ليومه
        b_det_prn = self.mk_btn(bar, "🖨 طباعة التقرير",
                                lambda: self.print_day_report(d, reprint=True), "#334155")
        b_det_prn.pack(side="right", padx=6)
        add_tip(b_det_prn, "طباعة تقرير إغلاق هذا اليوم على الطابعة الحرارية (إعادة طباعة)")
        # ★ إضافة (إصدار 7 — الميزة 8): زر «🖨 طباعة/معاينة A4» بجانب الأزرار
        # الموجودة في نافذة تفاصيل اليوم — يفتح نافذة المعاينة أولاً (تقرير
        # إغلاق اليوم بمسار A4/PDF الجديد بنفس محتوى التقرير الحراري)
        b_det_a4 = self.mk_btn(bar, "🖨 طباعة/معاينة A4",
                               lambda: self.open_print_preview("day", d), "#1d4ed8")
        b_det_a4.pack(side="right", padx=6)
        add_tip(b_det_a4, "معاينة تقرير هذا اليوم ثم طباعته على A4 عبر ملف PDF قياسي (أو حرارية 80mm من نفس النافذة)")

        # ★ إضافة (إصدار 8 — الميزة 4): نفس المبدأ في نافذة تفاصيل اليوم —
        # أزرار الإجراءات تُجمع في زر «⚙️ إجراءات» واحد (زر «إغلاق» النافذة
        # يُنشأ بعد هذا السطر فيبقى ظاهراً كما هو) بنفس الدوال ونفس المنطق
        # تماماً — تعديل ضروري محدود في التخطيط صرّحت به المواصفة
        det_action_btns = [w for w in bar.winfo_children() if isinstance(w, tk.Button)]
        for w in det_action_btns:
            w.pack_forget()
        b_det_menu = self.mk_btn(bar, "⚙️ إجراءات",
                                 lambda: self.show_day_details_menu(d, rows, rep, b_det_menu),
                                 "#334155")
        b_det_menu.pack(side="right", padx=6)
        add_tip(b_det_menu, "كل إجراءات هذا اليوم: تصدير CSV • تصدير Excel • طباعة حرارية • طباعة/معاينة A4")
        self.mk_btn(bar, "إغلاق", win.destroy, "#475569").pack(side="right", padx=6)
        # ★ إضافة (إصدار 4 — ميزة 5): تلميحات أزرار التصدير في نافذة التفاصيل
        for w in bar.winfo_children():
            if isinstance(w, tk.Button):
                t = w.cget("text")
                if t == "📥 تصدير CSV":
                    add_tip(w, "تصدير عمليات هذا اليوم إلى ملف CSV")
                elif t == "📊 تصدير Excel":
                    add_tip(w, "تصدير تفاصيل هذا اليوم إلى Excel")
                elif t == "إغلاق":
                    add_tip(w, "إغلاق نافذة التفاصيل")

    def show_day_details_menu(self, d, rows, rep, btn):
        """★ إضافة (إصدار 8 — الميزة 4): قائمة إجراءات نافذة تفاصيل اليوم —
        نفس الخيارات الموجودة سابقاً كأزرار بنفس الدوال ونفس المنطق تماماً"""
        m = tk.Menu(self, tearoff=0, bg=CARD, fg=DARK, font=("Segoe UI", 10),
                    activebackground=ACCENT, activeforeground="white", bd=0, relief="flat")
        if self.has_permission("export_reports"):
            m.add_command(label="📥 تصدير CSV", command=lambda: self.export_ops_csv(d, rows, rep))
            m.add_command(label="📊 تصدير Excel", command=lambda: self.export_day_xlsx(d, rows, rep))
        m.add_command(label="🖨 طباعة التقرير (حرارية)",
                      command=lambda: self.print_day_report(d, reprint=True))
        m.add_command(label="🖨 طباعة/معاينة A4",
                      command=lambda: self.open_print_preview("day", d))
        try:
            m.tk_popup(btn.winfo_rootx(), btn.winfo_rooty() + btn.winfo_height())
        finally:
            m.grab_release()

    def export_selected_day(self):
        sel = self.tv_arch.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر يوماً من الجدول أولاً"); return
        d = sel[0]
        with connect() as conn:
            rep = conn.execute("SELECT * FROM daily_reports WHERE report_date=?", (d,)).fetchone()
            # ★ تعديل ضروري معلن (إصدار 3 — ميزة 4): البائع يصدّر عملياته فقط من تفاصيل اليوم
            q = "SELECT * FROM operations WHERE date=?"
            params = [d]
            if self.role != "مدير":
                q += " AND seller_name=?"
                params.append(self.user_name)
            q += " ORDER BY id"
            rows = conn.execute(q, params).fetchall()
        self.export_ops_csv(d, rows, rep)

    def reopen_day(self):
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «إعادة فتح يوم مغلق» بدل «المدير فقط»
        if not self.require_admin("reopen_day"):
            return
        sel = self.tv_arch.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر يوماً من الجدول أولاً"); return
        d = sel[0]
        if not messagebox.askyesno("تأكيد", f"إعادة فتح يوم {d} سيحذف تقريره النهائي (تبقى العمليات).\nهل تريد المتابعة؟"):
            return
        with connect() as conn:
            conn.execute("DELETE FROM daily_reports WHERE report_date=?", (d,))
        audit("إعادة فتح يوم", d)               # ★ إضافة (ميزة 2): تسجيل إعادة الفتح
        self.refresh_archive(); self.refresh_today(); self.update_closed_banner(); self.refresh_stats()
        messagebox.showinfo("تم", f"أصبح يوم {d} مفتوحاً من جديد.\nيمكنك إضافة عمليات عليه ثم إغلاقه مرة أخرى.")

    def show_archive_menu(self):
        """★ إضافة (إصدار 8 — الميزة 4): قائمة إجراءات الأرشيف المنسدلة — كل
        الخيارات الموجودة سابقاً كأزرار، بنفس الدوال ونفس المنطق تماماً؛
        خيارات التصدير وإعادة الفتح تظهر بحسب الصلاحيات الفعلية"""
        m = tk.Menu(self, tearoff=0, bg=CARD, fg=DARK, font=("Segoe UI", 10),
                    activebackground=ACCENT, activeforeground="white", bd=0, relief="flat")
        m.add_command(label="📄 عرض تفاصيل اليوم", command=self.open_selected_day)
        if self.has_permission("export_reports"):
            m.add_command(label="🖨 طباعة/معاينة A4", command=self.print_selected_day_a4)
            m.add_command(label="📥 تصدير اليوم إلى CSV", command=self.export_selected_day)
            m.add_command(label="📊 تصدير الأرشيف كاملاً Excel", command=self.export_archive_xlsx)
            m.add_command(label="📄 تقرير الفترة A4", command=self.print_period_report)
        m.add_command(label="🖨 طباعة التقرير (حرارية)", command=self.print_selected_day)
        m.add_separator()
        if self.has_permission("reopen_day"):
            m.add_command(label="🔓 إعادة فتح اليوم", command=self.reopen_day)
        try:
            btn = self.arch_menu_btn
            m.tk_popup(btn.winfo_rootx(), btn.winfo_rooty() + btn.winfo_height())
        finally:
            m.grab_release()

    def export_ops_csv(self, d, rows, rep=None):
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «تصدير التقارير (CSV/Excel/PDF)»
        if not self.has_permission("export_reports"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «تصدير التقارير»")
            return
        path = filedialog.asksaveasfilename(title="حفظ التقرير", defaultextension=".csv",
                                            initialfile=f"تقرير_{d}.csv", filetypes=[("ملف CSV", "*.csv")])
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            # ★ تعديل ضروري معلن (ميزة 5): رأس الجدول وصفوفه أصبحا يشملان عمود العميل
            # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): أصبحا يشملان عمود البائع أيضاً
            w.writerow(["التاريخ", "اسم الصنف", "العميل", "البائع", "الكمية", "السعر", "المبيع", "النوع"])
            for r in rows:
                w.writerow([r["date"], r["item_name"], (r["customer_name"] or ""),
                            (r["seller_name"] or "—"),
                            r["quantity"], r["price"], r["total"], r["type"]])
            if rep:
                w.writerow([])
                w.writerow(["عدد العمليات", rep["ops_count"]])
                # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): ملخص التصدير يعرض
                # نقداً وشبكة منفصلين مع إجمالي المبيعات المجمع
                w.writerow(["نقداً", rep["total_cash"] or 0.0])
                w.writerow(["شبكة", rep["total_network"] or 0.0])
                w.writerow(["المبيعات (نقداً + شبكة)", rep["total_sales"]])
                w.writerow(["المرتجعات", rep["total_returns"]])
                w.writerow(["الإجمالي", rep["net_total"]])
        audit("تصدير CSV", f"{os.path.basename(path)} — {len(rows)} صف")   # ★ إضافة (ميزة 2)
        messagebox.showinfo("تم", "تم تصدير التقرير ✅\nيمكن فتحه مباشرة في Excel")

    # ---------- البحث ----------
    def build_search_page(self, p):
        self.page_head(p, "🔎 بحث", "ابحث عن صنف في كل العمليات منذ بداية الاستخدام")
        bar = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        bar.pack(fill="x", padx=25, pady=8)
        self.e_search = tk.Entry(bar, font=F, justify="center", relief="solid", bd=1)
        self.e_search.pack(side="right", fill="x", expand=True, ipady=7, padx=12, pady=12)
        self.e_search.bind("<Return>", lambda e: self.do_search())
        self.mk_btn(bar, "بحث", self.do_search).pack(side="left", padx=12)

        # ★ تعديل ضروري معلن (إصدار 4 — ميزة 1): الملاحظة تُنشأ دائماً وتُخفى للمدير —
        # لتتكيف الشاشة عند تبديل المستخدم دون إعادة بنائها
        # ★ إضافة (إصدار 3 — ميزة 4): البائع يبحث في عملياته فقط
        self.lbl_search_only = tk.Label(p, text="تُعرض عملياتك فقط", bg=BG, fg=GRAY,
                                        font=("Segoe UI", 10, "bold"))
        if self.role != "مدير":
            self.lbl_search_only.pack(fill="x", padx=25, anchor="e")

        self.lbl_search = tk.Label(p, text="", bg=BG, fg=ACCENT, font=FB)
        self.lbl_search.pack(fill="x", padx=25)

        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): عمود البائع في نتائج البحث
        frm, self.tv_search = self.mk_tree(p,
            ["النوع", "المبيع", "السعر", "الكمية", "اسم الصنف", "العميل", "البائع", "التاريخ"],
            [80, 110, 100, 80, 190, 130, 100, 100])
        frm.pack(fill="both", expand=True, padx=25, pady=8)
        self.tv_search.tag_configure("ret", foreground=RED)

    def do_search(self):
        q = self.e_search.get().strip()
        if not q:
            return
        self.tv_search.delete(*self.tv_search.get_children())
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 4): البائع يجد في عملياته فقط
        sql = "SELECT * FROM operations WHERE item_name LIKE ?"
        params = [f"%{q}%"]
        if self.role != "مدير":
            sql += " AND seller_name=?"
            params.append(self.user_name)
        sql += " ORDER BY date DESC, id DESC"
        with connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        total = 0
        for r in rows:
            total += r["total"]
            self.tv_search.insert("", "end", tags=(("ret",) if r["type"] == "مرتجع" else ()),
                values=(r["type"], money(r["total"]), money(r["price"]),
                        f'{r["quantity"]:g}', r["item_name"],
                        (r["customer_name"] or ""),
                        (r["seller_name"] or "—"), r["date"]))   # ★ ميزة 3+5 (إصدار 3): عمودا العميل والبائع
        self.lbl_search.config(text=f"نتائج «{q}»: {len(rows)} عملية — الإجمالي الكلي: {money(total)}")

    # ---------- الخروج والنسخ الاحتياطي ----------
    def backup_now(self):
        try:
            shutil.copy2(DB, BACKUP)
            audit("نسخة احتياطية", BACKUP)      # ★ إضافة (ميزة 2): تسجيل النسخ الاحتياطي
            messagebox.showinfo("تم", f"تم إنشاء نسخة احتياطية:\n{BACKUP}")
        except Exception as e:
            messagebox.showerror("خطأ", f"تعذر إنشاء النسخة:\n{e}")

    def exit_app(self):
        try:
            shutil.copy2(DB, BACKUP)
        except Exception:
            pass
        self.destroy()

    # ═══════════════════════════════════════════════════════════
    # ★★★ إضافات الإصدار 2 — دوال جديدة داخل الكلاس ★★★
    # ═══════════════════════════════════════════════════════════

    # ---------- (ميزة 1) بوابة الصلاحيات ----------
    # ★ إضافة (إصدار 8 — الميزة 5): دالة الفحص الدقيق للصلاحيات — بديل فحوصات
    # «المدير فقط» السابقة (هذا هو الاستبدال المصرح به في قواعد هذه الجلسة
    # لأنه جوهر نظام الصلاحيات): المدير يملك كل الصلاحيات دائماً، والبائع
    # بحسب ما منحه المدير له (تُقرأ صلاحياته من قاعدة البيانات فتسري
    # التعديلات فوراً حتى أثناء الجلسة)، والصلاحية الخاصة «manager» معناها:
    # للمدير فقط (مثل شاشة إدارة المستخدمين)
    def has_permission(self, key):
        if self.role == "مدير":
            return True
        if key == "manager":
            return False
        row = get_user_row(self.user_name)
        try:
            perms = json.loads(row["permissions"] or "[]") if row is not None else []
        except Exception:
            perms = []
        return key in perms

    def require_admin(self, perm="manager"):
        """★ تعديل مصرح به (إصدار 8 — الميزة 5): بوابة الصلاحيات الدقيقة —
        كانت تفحص «المدير فقط» والآن تفحص has_permission(الصلاحية) بدلاً منها
        (هذا هو الاستبدال المصرح به في قواعد هذه الجلسة لأنه جوهر نظام
        الصلاحيات) — والصلاحية الافتراضية «manager» تعني: للمدير فقط"""
        if self.has_permission(perm):
            return True
        messagebox.showwarning("صلاحية", "ليست لديك الصلاحية لهذا الإجراء")
        return False

    # ★ إضافة (إصدار 8 — الميزة 3): التتبع المركزي للنوافذ المفتوحة —
    # كل نافذة Toplevel تُفتح تُسجل هنا، وتُغلق كلها فوراً عند تبديل المستخدم
    def register_window(self, win):
        """تسجيل نافذة Toplevel في قائمة التتبع المركزية"""
        self.open_windows.append(win)
        win.bind("<Destroy>", lambda e: self._unregister_window(win), add="+")
        return win

    def _unregister_window(self, win):
        """إزالة نافذة من قائمة التتبع بعد إغلاقها"""
        try:
            if win in self.open_windows:
                self.open_windows.remove(win)
        except Exception:
            pass

    def close_all_windows(self):
        """إغلاق كل النوافذ المفتوحة فوراً (destroy) وإرجاع عددها —
        أول خطوة عند تبديل المستخدم قبل إظهار نافذة الدخول، فلا تبقى أي
        شاشة تعمل باسم المستخدم القديم بعد التبديل أبداً"""
        n = 0
        for w in list(getattr(self, "open_windows", [])):
            try:
                w.destroy()
                n += 1
            except Exception:
                pass
        self.open_windows = []
        return n

    # ---------- (ميزة 6) شاشة الفاتورة متعددة الأصناف ----------
    def show_invoice(self):
        """★ إضافة (ميزة 6): فتح شاشة الفاتورة وتحديث قائمة الأصناف"""
        self.show_page("invoice")
        self.refresh_items()

    def build_invoice_page(self, p):
        self.page_head(p, "🧾 فاتورة أصناف", "أدخل عدة أصناف ثم احفظ الفاتورة كاملة دفعة واحدة")

        form = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        form.pack(fill="x", padx=25, pady=8)

        def frow(label, width=18):
            fr = tk.Frame(form, bg=CARD); fr.pack(fill="x", padx=22, pady=6)
            tk.Label(fr, text=label, bg=CARD, fg=DARK, font=FB, width=width, anchor="e").pack(side="right")
            inner = tk.Frame(fr, bg=CARD)
            inner.pack(side="right", padx=(0, 10))
            return inner

        i_c = frow("اسم العميل (اختياري):", 20)
        self.e_inv_customer = tk.Entry(i_c, font=F, justify="center", relief="solid", bd=1, width=30)
        self.e_inv_customer.pack(side="right", ipady=4)

        i_i = frow("اسم الصنف:")
        self.cb_inv_item = ttk.Combobox(i_i, font=F, width=30)
        self.cb_inv_item.pack(side="right", ipady=4)

        i_q = frow("الكمية:")
        self.e_inv_qty = tk.Entry(i_q, font=F, justify="center", relief="solid", bd=1, width=30)
        self.e_inv_qty.pack(side="right", ipady=4)

        i_p = frow("السعر:")
        self.e_inv_price = tk.Entry(i_p, font=F, justify="center", relief="solid", bd=1, width=30)
        self.e_inv_price.pack(side="right", ipady=4)

        trow = tk.Frame(form, bg=CARD); trow.pack(fill="x", padx=22, pady=8)
        tk.Label(trow, text="النوع:", bg=CARD, fg=DARK, font=FB).pack(side="right")
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): ثلاثة أنواع في صفحة الفاتورة أيضاً —
        # نقداً (أخضر) / شبكة (أزرق) بقيمة موجبة، ومرتجع (أحمر) بقيمة سالبة كما هو
        self.inv_type_var = tk.StringVar(value="نقداً")
        for txt, col in [("نقداً", GREEN), ("شبكة", ACCENT), ("مرتجع", RED)]:
            tk.Radiobutton(trow, text=txt, variable=self.inv_type_var, value=txt, font=FB,
                           fg=col, bg=CARD, selectcolor="#dbeafe", activebackground=CARD,
                           activeforeground=col, indicatoron=0, width=10, bd=1,
                           relief="solid", cursor="hand2").pack(side="right", padx=10)

        crow = tk.Frame(form, bg=CARD); crow.pack(fill="x", padx=22, pady=(2, 12))
        self.mk_btn(crow, "➕ إضافة إلى السلة", self.add_to_cart, GREEN).pack(side="right")
        self.lbl_inv_status = tk.Label(crow, text="", bg=CARD, font=FB)
        self.lbl_inv_status.pack(side="right", padx=14)

        frm, self.tv_cart = self.mk_tree(p,
            ["النوع", "المبيع", "السعر", "الكمية", "الصنف"],
            [90, 120, 110, 90, 240])
        frm.pack(fill="both", expand=True, padx=25, pady=8)
        self.tv_cart.tag_configure("ret", foreground=RED)

        # ★ إجمالي السلة لحظياً — يتحدث مع كل إضافة/إزالة
        self.lbl_inv_total = tk.Label(p, text="إجمالي السلة: 0.00", bg=BG, fg=ACCENT, font=FV)
        self.lbl_inv_total.pack(fill="x", padx=25)

        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25, pady=(0, 18))
        self.mk_btn(bar, "🗑 إزالة المحدد من السلة", self.remove_from_cart, RED).pack(side="right", padx=6)
        self.mk_btn(bar, "💾 حفظ الفاتورة كاملة", self.save_invoice, ORANGE).pack(side="left", padx=6)

        self.cart = []   # السلة: قائمة الأصناف قبل الحفظ
        for w in (self.e_inv_qty, self.e_inv_price):
            w.bind("<Return>", lambda e: self.add_to_cart())
        self.cb_inv_item.bind("<Return>", lambda e: self.add_to_cart())

    def add_to_cart(self):
        """★ إضافة (ميزة 6): التحقق ثم إضافة الصنف الحالي إلى السلة"""
        item = self.cb_inv_item.get().strip()
        if not item:
            messagebox.showwarning("تنبيه", "اكتب اسم الصنف أولاً"); return
        q  = to_num(self.e_inv_qty.get())
        pr = to_num(self.e_inv_price.get())
        if q is None or q <= 0:
            messagebox.showwarning("تنبيه",
                f"الكمية غير صحيحة: «{self.e_inv_qty.get()}»\nأدخل رقماً أكبر من صفر"); return
        if pr is None or pr < 0:
            messagebox.showwarning("تنبيه",
                f"السعر غير صحيح: «{self.e_inv_price.get()}»\nأدخل رقماً صحيحاً"); return
        t = self.inv_type_var.get()
        total = q * pr
        if t == "مرتجع":
            total = -total          # المرتجع في السلة أيضاً بقيمة سالبة
        self.cart.append({"item": item, "qty": q, "price": pr, "total": total, "type": t})
        self.e_inv_qty.delete(0, "end"); self.e_inv_price.delete(0, "end")
        self.cb_inv_item.set("")
        self.update_cart_view()
        self.lbl_inv_status.config(text=f"✔ أُضيف إلى السلة ({t}: {item})", fg=GREEN)

    def remove_from_cart(self):
        """★ إضافة (ميزة 6): إزالة صنف محدد من السلة قبل الحفظ"""
        sel = self.tv_cart.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر صنفاً من السلة أولاً"); return
        removed = self.cart.pop(int(sel[0]))
        self.update_cart_view()
        self.lbl_inv_status.config(text=f"🗑 أُزيل من السلة: {removed['item']}", fg=RED)

    def update_cart_view(self):
        """★ إضافة (ميزة 6): إعادة رسم جدول السلة والإجمالي اللحظي"""
        self.tv_cart.delete(*self.tv_cart.get_children())
        for i, it in enumerate(self.cart):
            self.tv_cart.insert("", "end", iid=str(i),
                tags=(("ret",) if it["type"] == "مرتجع" else ()),
                values=(it["type"], money(it["total"]), money(it["price"]),
                        f'{it["qty"]:g}', it["item"]))
        tot = sum(it["total"] for it in self.cart)
        self.lbl_inv_total.config(text=f"إجمالي السلة: {money(tot)}",
                                  fg=(ACCENT if tot >= 0 else RED))

    def save_invoice(self):
        """★ إضافة (ميزة 6): تأكيد بالمجموع ثم حفظ كل الأصناف دفعة واحدة كعمليات اليوم"""
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «إضافة عمليات وفواتير» — الفحص
        # الدقيق الجديد (المدير يملك كل الصلاحيات دائماً ولا يلاحظ الفرق)
        if not self.has_permission("add_ops"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «إضافة عمليات وفواتير»")
            return
        d = today_str()
        if is_closed(d):
            messagebox.showwarning("اليوم مغلق",
                "تم إغلاق اليوم وحفظ تقريره.\nلا يمكن حفظ فاتورة على يوم مغلق.\n"
                "➡ يمكنك إعادة فتح اليوم من شاشة الأرشيف.")
            return
        if not self.cart:
            messagebox.showwarning("السلة فارغة", "أضف صنفاً واحداً على الأقل إلى السلة أولاً"); return
        cust = self.e_inv_customer.get().strip()
        total = sum(it["total"] for it in self.cart)
        if not messagebox.askyesno("تأكيد حفظ الفاتورة",
                f"عدد الأصناف: {len(self.cart)}\nالمجموع: {money(total)}\n"
                + (f"العميل: {cust}\n" if cust else "")
                + f"\nسيُحفظ كل صنف كعملية على يوم {d}.\nهل تريد المتابعة؟"):
            return
        snapshot = list(self.cart)   # نسخة للتصدير بعد تفريغ السلة
        try:
            with connect() as conn:   # ★ معاملة واحدة: كل الأصناف تُحفظ وتُلتزم دفعة واحدة
                for it in snapshot:
                    # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): كل صنف يُسجل باسم البائع الحالي
                    conn.execute("INSERT INTO operations(date,item_name,quantity,price,total,type,customer_name,seller_name)"
                                 " VALUES(?,?,?,?,?,?,?,?)",
                                 (d, it["item"], it["qty"], it["price"], it["total"], it["type"],
                                  cust, CURRENT_USER["name"]))
        except Exception as e:
            messagebox.showerror("خطأ في الحفظ", f"تعذر حفظ الفاتورة:\n{e}")
            return
        # ★ إضافة (إصدار 5 — نظام الأنواع الثلاثة): تفاصيل التدقيق تذكر الأنواع
        # (مثل: حفظ فاتورة — 3 صنف — المجموع 1,500.00 — الأنواع: نقداً 2، شبكة 1)
        tset = {}
        for it in snapshot:
            tset[it["type"]] = tset.get(it["type"], 0) + 1
        audit("حفظ فاتورة", f"{len(snapshot)} صنف — المجموع {money(total)} — الأنواع: "
              + "، ".join(f"{k} {v}" for k, v in tset.items())
              + (f" | عميل: {cust}" if cust else ""))   # ★ إضافة (ميزة 2)
        self.cart = []                          # السلة تُفرغ بعد الحفظ
        self.e_inv_customer.delete(0, "end")
        # ★ إضافة (إصدار 5): عودة الاختيار تلقائياً إلى «نقداً» بعد حفظ الفاتورة
        self.inv_type_var.set("نقداً")
        self.update_cart_view()
        self.refresh_items(); self.refresh_today(); self.refresh_stats()
        self.lbl_inv_status.config(text=f"✔ تم حفظ الفاتورة ({len(snapshot)} صنف)", fg=GREEN)
        if messagebox.askyesno("تم", "تم حفظ الفاتورة كاملة ✅\nهل تريد تصديرها إلى Excel الآن؟"):
            self.export_invoice_xlsx(snapshot, cust)

    def export_invoice_xlsx(self, items, cust=""):
        """★ إضافة (ميزة 3+6): تصدير الفاتورة الحالية إلى Excel حقيقي"""
        path = filedialog.asksaveasfilename(title="حفظ الفاتورة", defaultextension=".xlsx",
                                            initialfile=f"فاتورة_{today_str()}.xlsx",
                                            filetypes=[("ملف Excel", "*.xlsx")])
        if not path:
            return
        d = today_str()
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): عمود البائع في تصدير الفاتورة
        headers = ["التاريخ", "العميل", "الصنف", "الكمية", "السعر", "المبيع", "النوع", "البائع"]
        widths  = [12, 20, 26, 10, 10, 12, 10, 16]
        rows = [[d, cust or "", it["item"], it["qty"], it["price"], it["total"], it["type"],
                 CURRENT_USER["name"]] for it in items]
        export_xlsx(path, headers, rows, widths,
                    desc=f"فاتورة {len(items)} صنف — المجموع {money(sum(it['total'] for it in items))}")

    # ---------- (ميزة 2) شاشة سجل التدقيق ----------
    def show_audit(self):
        """★ إضافة (ميزة 2): فتح سجل التدقيق — للمدير فقط"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «عرض سجل التدقيق» بدل «المدير فقط»
        if not self.require_admin("view_audit"):
            return
        self.show_page("audit")
        self.refresh_audit()

    def build_audit_page(self, p):
        self.page_head(p, "📜 سجل التدقيق", "تسجيل تلقائي لكل الإجراءات — للمدير فقط")
        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25)
        self.mk_btn(bar, "🔄 تحديث", self.refresh_audit, "#475569").pack(side="left", pady=6)

        # ★ إضافة (إصدار 8 — الميزة 1): السجل التفاعلي — قائمة «الإجراء» المنسدلة
        # تختصر الفلترة الشائعة بدون بحث، وزر «عرض الكل» يلغي الفلتر ويعيد
        # الجدول كاملاً (الفلترة عرضية في الذاكرة فقط ولا تمس قاعدة البيانات)
        self.audit_filter = None      # None أو ("user", اسم) أو ("action", إجراء)
        self.audit_all_rows = []      # كل السجلات في الذاكرة (يُفلتر العرض منها فقط)
        b_audit_all = self.mk_btn(bar, "👁 عرض الكل", self.clear_audit_filter, "#0d9488")
        b_audit_all.pack(side="left", padx=6, pady=6)
        add_tip(b_audit_all, "إعادة الجدول كاملاً وإلغاء الفلتر النشط")
        fr_act = tk.Frame(bar, bg=BG); fr_act.pack(side="right", padx=6)
        tk.Label(fr_act, text="الإجراء:", bg=BG, fg=DARK, font=FB).pack(side="right", padx=4)
        self.cb_audit_action = ttk.Combobox(fr_act, font=F, width=22, state="readonly",
                                            values=["كل الإجراءات"])
        self.cb_audit_action.current(0)
        self.cb_audit_action.pack(side="right", ipady=3)
        self.cb_audit_action.bind("<<ComboboxSelected>>",
                                  lambda e: self.apply_audit_action_filter())
        add_tip(self.cb_audit_action, "فلترة سريعة حسب نوع الإجراء — والنقر على أي صف يفلتر أيضاً")

        # ★ سطر الفلتر النشط الملون فوق الجدول: «🔍 سجلات: [الاسم/الإجراء] (عدد)»
        self.lbl_audit_filter = tk.Label(p, text="", bg=BG, fg=GRAY, font=FB, anchor="e")
        self.lbl_audit_filter.pack(fill="x", padx=25)

        frm, self.tv_audit = self.mk_tree(p,
            ["التفاصيل", "الإجراء", "المستخدم", "التاريخ والوقت"],
            [380, 150, 100, 160])
        frm.pack(fill="both", expand=True, padx=25, pady=8)
        # ★ النقر على صف: عمود «المستخدم» (أو أي مكان بالصف) يعرض سجلات هذا
        # المستخدم فقط، والنقر على عمود «الإجراء» يعرض هذا الإجراء فقط
        # (كل من حفظ فاتورة مثلاً) — فلترة عرضية في الذاكرة فقط
        self.tv_audit.bind("<ButtonRelease-1>", self.on_audit_click)
        add_tip(self.tv_audit, "انقر أي صف للفلترة حسب المستخدم — وانقر عمود «الإجراء» للفلترة حسب الإجراء")
        self.refresh_audit()

    def refresh_audit(self):
        """★ إضافة (ميزة 2): عرض أحدث الإجراءات أولاً"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): فحص الصلاحية الدقيقة بدل «المدير فقط»
        if not self.has_permission("view_audit"):
            return
        self.tv_audit.delete(*self.tv_audit.get_children())
        with connect() as conn:
            rows = conn.execute("SELECT * FROM audit_log ORDER BY id DESC").fetchall()
        # ★ إضافة (إصدار 8 — الميزة 1): السجلات كلها تُحفظ في الذاكرة أولاً —
        # الفلترة التفاعلية عرضية فقط (في الذاكرة) ولا تمس قاعدة البيانات،
        # وقائمة «الإجراء» المنسدلة تتحدث بأنواع الإجراءات المتاحة
        self.audit_all_rows = rows
        self.update_audit_action_values(rows)
        for r in rows:
            self.tv_audit.insert("", "end", values=(r["details"], r["action"], r["username"], r["ts"]))
        # ★ إضافة (إصدار 8 — الميزة 1): العرض يمر بالفلتر النشط (إن وُجد)
        self.render_audit()

    # ★ إضافة (إصدار 8 — الميزة 1): دوال السجل التفاعلي — فلترة عرضية بالنقر
    def update_audit_action_values(self, rows):
        """تحديث قائمة «الإجراء» المنسدلة من السجلات المعروضة (بدون تكرار)"""
        acts = sorted({r["action"] for r in rows})
        self.cb_audit_action["values"] = ["كل الإجراءات"] + acts
        if self.cb_audit_action.get() not in self.cb_audit_action["values"]:
            self.cb_audit_action.set("كل الإجراءات")

    def render_audit(self):
        """عرض السجلات مع الفلتر النشط — سطر ملون فوق الجدول يوضح الفلتر
        وعدد السجلات المعروضة (الفلترة في الذاكرة فقط ولا تمس القاعدة)"""
        f = self.audit_filter
        rows = self.audit_all_rows
        if f is not None:
            key, val = f
            rows = [r for r in rows if (r["username"] == val if key == "user"
                                        else r["action"] == val)]
            kind = "المستخدم" if key == "user" else "الإجراء"
            self.lbl_audit_filter.config(
                text=f"🔍 سجلات: {kind} = {val}   ({len(rows)} سجلاً) — اضغط «👁 عرض الكل» لإلغاء الفلتر",
                bg="#dbeafe", fg="#1e3a8a")
        else:
            self.lbl_audit_filter.config(
                text=f"🔍 السجلات: الكل   ({len(rows)} سجلاً)", bg=BG, fg=GRAY)
        self.tv_audit.delete(*self.tv_audit.get_children())
        for r in rows:
            self.tv_audit.insert("", "end", values=(r["details"], r["action"],
                                                    r["username"], r["ts"]))

    def on_audit_click(self, event):
        """النقر على صف: فلترة حسب المستخدم — والنقر على عمود «الإجراء»:
        فلترة بهذا الإجراء فقط (كل من حفظ فاتورة مثلاً)"""
        row_id = self.tv_audit.identify_row(event.y)
        if not row_id:
            return
        col = self.tv_audit.identify_column(event.x)   # #1 التفاصيل، #2 الإجراء، #3 المستخدم
        vals = self.tv_audit.item(row_id, "values")
        if col == "#2":                    # عمود «الإجراء»
            self.audit_filter = ("action", vals[1])
        else:                              # أي مكان آخر بالصف → فلترة بالمستخدم
            self.audit_filter = ("user", vals[2])
        self.render_audit()

    def apply_audit_action_filter(self):
        """تطبيق الفلتر السريع من قائمة «الإجراء» المنسدلة"""
        val = self.cb_audit_action.get()
        self.audit_filter = None if val in ("كل الإجراءات", "") else ("action", val)
        self.render_audit()

    def clear_audit_filter(self):
        """«عرض الكل»: إعادة الجدول كاملاً وإلغاء الفلتر"""
        self.audit_filter = None
        self.cb_audit_action.set("كل الإجراءات")
        self.render_audit()

    # ---------- (ميزة 1) تغيير كلمة المرور ----------
    def change_password_dialog(self):
        """★ تعديل ضروري معلن (إصدار 3 — ميزة 7): تغيير كلمة المرور لأي مستخدم —
        يغيّر كلمة مروره هو في جدول users
        (وإعادة تعيين كلمات البائعين تكون من شاشة إدارة المستخدمين)"""
        # ★ إضافة (إصدار 8 — الميزة 3): تسجيل النافذة في التتبع المركزي
        win = self.register_window(tk.Toplevel(self))
        win.title("تغيير كلمة المرور")
        win.geometry("420x380"); win.configure(bg=BG); win.resizable(False, False)
        card = tk.Frame(win, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=16)
        tk.Label(card, text="🔑 تغيير كلمة المرور", bg=CARD, fg=DARK, font=FT).pack(pady=(14, 4))
        # ★ إضافة (إصدار 3 — ميزة 7): إظهار الحساب الحالي الذي ستُغيّر كلمة مروره
        tk.Label(card, text=f"الحساب الحالي: {self.user_name}", bg=CARD, fg=GRAY,
                 font=("Segoe UI", 10)).pack(pady=(0, 8))

        def row(label):
            fr = tk.Frame(card, bg=CARD); fr.pack(fill="x", padx=18, pady=5)
            tk.Label(fr, text=label, bg=CARD, fg=DARK, font=FB, width=18, anchor="e").pack(side="right")
            e = tk.Entry(fr, font=F, justify="center", show="•", relief="solid", bd=1, width=22)
            e.pack(side="right", padx=(0, 8), ipady=4)
            return e

        e_cur = row("كلمة المرور الحالية:")
        e_new = row("كلمة المرور الجديدة:")
        # ★ إضافة (إصدار 9 — الميزة 4): شريط قوة كلمة المرور الجديدة تحت حقلها
        # مباشرة — يتحدث مع كل ضغطة مفتاح (أحمر/برتقالي/أخضر + النص الإرشادي)
        strength_update = make_strength_bar(card)
        e_new.bind("<KeyRelease>", lambda _e: strength_update(e_new.get()))
        e_con = row("تأكيد الجديدة:")
        # ★ إضافة (إصدار 9 — الميزة 1): زر عين 👁 داخل كل حقل كلمة مرور (على
        # يساره) — 👁 عند الإخفاء و🙈 عند الإظهار، ويعود للإخفاء تلقائياً بعد 5 ثوانٍ
        for _e in (e_cur, e_new, e_con):
            add_eye_to_entry(_e)

        def do_change():
            cur, new, con = e_cur.get(), e_new.get(), e_con.get()
            urow = get_user_row(self.user_name)
            if urow is None or not verify_user_password(urow, cur):
                messagebox.showerror("خطأ", "كلمة المرور الحالية غير صحيحة", parent=win); return
            # ★ تعديل مصرح به (إصدار 9 — الميزة 4): منع الحفظ إذا كانت ضعيفة جداً
            # (أقل من 5 أحرف = أحمر في شريط القوة) برسالة عربية واضحة —
            # كانت «4 أحرف على الأقل»
            if pw_is_weak(new):
                messagebox.showwarning("تنبيه", "كلمة المرور الجديدة ضعيفة جداً — استخدم 5 أحرف على الأقل", parent=win); return
            if new != con:
                messagebox.showwarning("تنبيه", "التأكيد لا يطابق كلمة المرور الجديدة", parent=win); return
            salt = secrets.token_hex(16)
            with connect() as conn:
                conn.execute("UPDATE users SET password_hash=? WHERE username=?",
                             (salt + "$" + hash_pwd(salt, new), self.user_name))
            audit("تغيير كلمة المرور", self.user_name)   # ★ إضافة (ميزة 2)
            messagebox.showinfo("تم", "تم تغيير كلمة المرور بنجاح", parent=win)
            win.destroy()

        self.mk_btn(card, "💾 حفظ", do_change, ACCENT).pack(pady=12)

    # ---------- (ميزة 4) التصفية بالمدى ----------
    def filter_archive(self):
        """★ إضافة (ميزة 4): عرض التقارير ضمن المدى + الإجمالي التراكمي"""
        f, t = parse_date_multi(self.e_from.get()), parse_date_multi(self.e_to.get())
        bad = [lbl for lbl, v in (("من تاريخ", f), ("إلى تاريخ", t)) if v is None]
        if bad:
            messagebox.showwarning("تاريخ خاطئ",
                "صيغة غير صحيحة لـ " + " و ".join(bad) +
                "\nالصيغ المقبولة: 2025-01-10 أو 10-01-2025 أو 10/01/2025")
            return
        sql, params, cond = "SELECT * FROM daily_reports", [], []
        if f:
            cond.append("report_date >= ?"); params.append(f)
        if t:
            cond.append("report_date <= ?"); params.append(t)
        if cond:
            sql += " WHERE " + " AND ".join(cond)
        sql += " ORDER BY report_date DESC"
        with connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        self.tv_arch.delete(*self.tv_arch.get_children())
        for r in rows:
            # ★ تعديل (إصدار 5): القيم تشمل نقداً وشبكة منفصلين
            self.tv_arch.insert("", "end", iid=r["report_date"], values=(
                r["closed_at"], money(r["net_total"]), money(r["total_returns"]),
                money(r["total_network"] or 0), money(r["total_cash"] or 0),
                r["ops_count"], r["report_date"]))
        self.update_arch_summary(rows)

    def show_all_archive(self):
        """★ إضافة (ميزة 4): مسح التصفية والعودة لعرض كل التقارير"""
        self.e_from.delete(0, "end")
        self.e_to.delete(0, "end")
        self.refresh_archive()

    def update_arch_summary(self, rows):
        """★ إضافة (ميزة 4): صف الإجمالي التراكمي لكل الأيام المعروضة حالياً
        ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): يعرض نقداً وشبكة منفصلين"""
        n   = len(rows)
        ca  = sum((r["total_cash"] or 0) for r in rows)
        nw  = sum((r["total_network"] or 0) for r in rows)
        rt  = sum((r["total_returns"] or 0) for r in rows)
        net = sum((r["net_total"] or 0) for r in rows)
        self.lbl_arch_summary.config(
            text=(f"الأيام المعروضة: {n} — نقداً: {money(ca)} — شبكة: {money(nw)} — "
                  f"المرتجعات: {money(rt)} — الإجمالي التراكمي: {money(net)}" if n else ""),
            fg=(GREEN if net >= 0 else RED))

    # ---------- (ميزة 3) تصدير Excel ----------
    def export_archive_xlsx(self):
        """★ إضافة (ميزة 3): تصدير كل تقارير الأرشيف إلى Excel حقيقي"""
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «تصدير التقارير (CSV/Excel/PDF)»
        if not self.has_permission("export_reports"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «تصدير التقارير»")
            return
        with connect() as conn:
            rows = conn.execute("SELECT * FROM daily_reports ORDER BY report_date DESC").fetchall()
        if not rows:
            messagebox.showinfo("تنبيه", "لا توجد تقارير محفوظة بعد"); return
        path = filedialog.asksaveasfilename(title="حفظ تقرير الأرشيف", defaultextension=".xlsx",
                                            initialfile=f"الأرشيف_كاملاً_{today_str()}.xlsx",
                                            filetypes=[("ملف Excel", "*.xlsx")])
        if not path:
            return
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): أعمدة نقداً وشبكة منفصلين
        headers = ["التاريخ", "عدد العمليات", "نقداً", "شبكة", "المرتجعات", "الإجمالي", "وقت الإغلاق"]
        widths  = [12, 12, 14, 14, 14, 14, 18]
        xrows = [[r["report_date"], r["ops_count"], r["total_cash"] or 0.0,
                  r["total_network"] or 0.0, r["total_returns"], r["net_total"],
                  r["closed_at"]] for r in rows]
        export_xlsx(path, headers, xrows, widths, desc=f"الأرشيف كاملاً — {len(rows)} تقريراً")
        messagebox.showinfo("تم", "تم تصدير الأرشيف إلى Excel ✅")

    def export_day_xlsx(self, d, rows, rep=None):
        """★ إضافة (ميزة 3): تصدير تفاصيل يوم واحد إلى Excel حقيقي مع الملخص"""
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «تصدير التقارير (CSV/Excel/PDF)»
        if not self.has_permission("export_reports"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «تصدير التقارير»")
            return
        path = filedialog.asksaveasfilename(title="حفظ التقرير", defaultextension=".xlsx",
                                            initialfile=f"تقرير_{d}.xlsx",
                                            filetypes=[("ملف Excel", "*.xlsx")])
        if not path:
            return
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 3): رأس الجدول وصفوفه أصبحا يشملان عمود البائع
        headers = ["التاريخ", "اسم الصنف", "العميل", "البائع", "الكمية", "السعر", "المبيع", "النوع"]
        widths  = [12, 26, 20, 16, 10, 10, 12, 10]
        xrows = [[r["date"], r["item_name"], (r["customer_name"] or ""), (r["seller_name"] or "—"),
                  r["quantity"], r["price"], r["total"], r["type"]] for r in rows]
        extra = None
        if rep:
            # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): ملخص Excel يعرض
            # نقداً وشبكة منفصلين مع إجمالي المبيعات المجمع
            extra = [("عدد العمليات", rep["ops_count"]), ("نقداً", rep["total_cash"] or 0.0),
                     ("شبكة", rep["total_network"] or 0.0),
                     ("المبيعات (نقداً + شبكة)", rep["total_sales"]),
                     ("المرتجعات", rep["total_returns"]), ("الإجمالي", rep["net_total"])]
        export_xlsx(path, headers, xrows, widths, desc=f"تقرير يوم {d} — {len(rows)} عملية", extra=extra)
        messagebox.showinfo("تم", "تم تصدير التقرير إلى Excel ✅")

    # ═════════════════════════════════════════════════════════
    # ★★★ إضافات الإصدار 3 — إدارة المستخدمين وتقرير أداء البائعين ★★★
    # ═════════════════════════════════════════════════════════

    # ---------- (ميزة 5) شاشة إدارة المستخدمين ----------
    def show_users(self):
        """★ إضافة (إصدار 3 — ميزة 5): فتح شاشة إدارة المستخدمين — للمدير فقط"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): إدارة المستخدمين والصلاحيات للمدير فقط
        if not self.require_admin("manager"):
            return
        self.show_page("users")
        self.refresh_users()

    def build_users_page(self, p):
        self.page_head(p, "👥 إدارة المستخدمين",
                       "إضافة البائعين وإيقافهم وتفعيلهم وإعادة تعيين كلمات المرور — للمدير فقط")
        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25)
        self.mk_btn(bar, "🔄 تحديث", self.refresh_users, "#475569").pack(side="left", pady=6)

        frm, self.tv_users = self.mk_tree(p,
            ["تاريخ الإضافة", "عدد العمليات", "الحالة", "الدور", "اسم المستخدم"],
            [150, 110, 90, 90, 170])
        frm.pack(fill="both", expand=True, padx=25, pady=8)

        bar2 = tk.Frame(p, bg=BG); bar2.pack(fill="x", padx=25, pady=(0, 18))
        self.mk_btn(bar2, "🚫 إيقاف / تفعيل", self.toggle_user_active, ORANGE).pack(side="left", padx=6)
        self.mk_btn(bar2, "🔑 إعادة تعيين كلمة المرور", self.reset_password_dialog,
                    "#7c3aed").pack(side="left", padx=6)
        # ★ إضافة (إصدار 8 — الميزة 5): زر تعديل الصلاحيات الدقيقة للمستخدم المحدد
        b_perms = self.mk_btn(bar2, "✏️ تعديل الصلاحيات", self.edit_permissions_dialog, "#0d9488")
        b_perms.pack(side="left", padx=6)
        add_tip(b_perms, "تعديل صلاحيات المستخدم المحدد — كل منح أو سحب يُسجل في سجل التدقيق")
        # ★ تعديل ضروري معلن (إصدار 8 — الميزة 5): الزر أصبح «إضافة مستخدم» لأن
        # النافذة تضيف مديراً أو بائعاً باختيار الدور (كانت لإضافة بائع فقط)
        self.mk_btn(bar2, "➕ إضافة مستخدم", self.add_user_dialog, GREEN).pack(side="right", padx=6)
        self.refresh_users()

    def refresh_users(self):
        """★ إضافة (إصدار 3 — ميزة 5): عرض كل الحسابات مع عدد عمليات كل مستخدم"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): إدارة المستخدمين للمدير فقط (فحص دقيق)
        if not self.has_permission("manager"):
            return
        self.tv_users.delete(*self.tv_users.get_children())
        with connect() as conn:
            rows = conn.execute("SELECT * FROM users ORDER BY id").fetchall()
            counts = dict((r[0], r[1]) for r in conn.execute(
                "SELECT seller_name, COUNT(*) FROM operations GROUP BY seller_name"))
        for r in rows:
            self.tv_users.insert("", "end", iid=str(r["id"]), values=(
                r["created_at"], counts.get(r["username"], 0),
                ("مفعل" if r["active"] else "موقوف"), r["role"], r["username"]))

    def add_user_dialog(self):
        """★ إضافة (إصدار 3 — ميزة 5): إضافة بائع باسم مستخدم غير مكرر وكلمة مرور (4 أحرف على الأقل)
        ★ إضافة (إصدار 8 — الميزة 5): أصبحت إضافة مستخدم (مدير/بائع) مع تحديد
        صلاحياته الدقيقة من مربعات الاختيار العشرة"""
        # ★ إضافة (إصدار 8 — الميزة 3): تسجيل النافذة في التتبع المركزي
        win = self.register_window(tk.Toplevel(self))
        # ★ تعديل ضروري معلن (إصدار 8 — الميزة 5): النافذة أصبحت «إضافة مستخدم»
        # وتوسّعت لاستيعاب اختيار الدور وصندوق الصلاحيات (كانت لإضافة بائع فقط)
        win.title("إضافة مستخدم")
        win.geometry("430x720"); win.configure(bg=BG); win.resizable(False, False)
        card = tk.Frame(win, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=16)
        # ★ تعديل ضروري معلن (إصدار 8 — الميزة 5): العنوان أصبح «إضافة مستخدم»
        tk.Label(card, text="➕ إضافة مستخدم", bg=CARD, fg=DARK, font=FT).pack(pady=(14, 10))

        def row(label, show=""):
            fr = tk.Frame(card, bg=CARD); fr.pack(fill="x", padx=18, pady=5)
            tk.Label(fr, text=label, bg=CARD, fg=DARK, font=FB, width=20, anchor="e").pack(side="right")
            e = tk.Entry(fr, font=F, justify="center", show=show, relief="solid", bd=1, width=22)
            e.pack(side="right", padx=(0, 8), ipady=4)
            return e

        e_name = row("اسم المستخدم:")
        e_pwd  = row("كلمة المرور:", "•")
        e_con  = row("تأكيد كلمة المرور:", "•")

        # ★ إضافة (إصدار 8 — الميزة 5): اختيار الدور (مدير/بائع) + صندوق
        # الصلاحيات العشر — البائع الافتراضي: «إضافة عمليات وفواتير» فقط،
        # والمدير يملك كل الصلاحيات دائماً (تُعلّم كلها وتُقفل تلقائياً)
        role_row = tk.Frame(card, bg=CARD); role_row.pack(fill="x", padx=18, pady=(8, 4))
        tk.Label(role_row, text="الدور:", bg=CARD, fg=DARK, font=FB, width=20,
                 anchor="e").pack(side="right")
        cb_role = ttk.Combobox(role_row, font=F, width=20, state="readonly",
                               values=["بائع", "مدير"], justify="center")
        cb_role.current(0)
        cb_role.pack(side="right", padx=(0, 8), ipady=4)
        add_tip(cb_role, "بائع: تُمنحه الصلاحيات التي تختارها — مدير: يملك كل الصلاحيات دائماً")
        perm_vars, perm_cbs = {}, {}
        for key, label in PERMISSIONS:
            v = tk.BooleanVar(value=(key == "add_ops"))   # الافتراضي للبائع: إضافة العمليات فقط
            cb = tk.Checkbutton(card, text=label, variable=v, font=("Segoe UI", 10),
                                bg=CARD, fg=DARK, selectcolor="#dbeafe",
                                activebackground=CARD, activeforeground=ACCENT,
                                anchor="e", justify="right", onvalue=True, offvalue=False)
            cb.pack(fill="x", padx=30, pady=1)
            perm_vars[key] = v
            perm_cbs[key] = cb
        lbl_perm_note = tk.Label(card, text="البائع الافتراضي: «إضافة عمليات وفواتير» فقط — المدير يمنح الباقي من «✏️ تعديل الصلاحيات»",
                                 bg=CARD, fg=GRAY, font=("Segoe UI", 9))
        lbl_perm_note.pack(pady=(4, 0))

        def on_role_change(_e=None):
            """المدير يملك كل الصلاحيات دائماً — تُقفل مربعاته عند اختيار دوره،
            والعودة إلى «بائع» تعيد الصلاحيات الافتراضية (إضافة العمليات فقط)"""
            if cb_role.get() == "مدير":
                for v in perm_vars.values():
                    v.set(True)
                for cb in perm_cbs.values():
                    cb.config(state="disabled")
                lbl_perm_note.config(text="🔒 المدير يملك كل الصلاحيات دائماً (مقفلة)")
            else:
                for key, v in perm_vars.items():
                    v.set(key == "add_ops")   # العودة للافتراضي: إضافة العمليات فقط
                for cb in perm_cbs.values():
                    cb.config(state="normal")
                lbl_perm_note.config(text="البائع الافتراضي: «إضافة عمليات وفواتير» فقط — المدير يمنح الباقي من «✏️ تعديل الصلاحيات»")
        cb_role.bind("<<ComboboxSelected>>", on_role_change)

        def do_add():
            name, p1, p2 = e_name.get().strip(), e_pwd.get(), e_con.get()
            if not name:
                messagebox.showwarning("تنبيه", "اكتب اسم المستخدم أولاً", parent=win); return
            if get_user_row(name) is not None:
                messagebox.showwarning("تنبيه", "اسم المستخدم موجود مسبقاً — اختر اسماً آخر", parent=win); return
            if len(p1) < 4:
                messagebox.showwarning("تنبيه", "كلمة المرور قصيرة جداً (4 أحرف على الأقل)", parent=win); return
            if p1 != p2:
                messagebox.showwarning("تنبيه", "التأكيد لا يطابق كلمة المرور", parent=win); return
            # ★ تعديل ضروري معلن (إصدار 8 — الميزة 5): الحفظ يشمل الدور المختار
            # والصلاحيات الممنوحة (كان يحفظ «بائع» فقط) — جوهر نظام الصلاحيات
            role = cb_role.get()
            perms = ([k for k, _ in PERMISSIONS] if role == "مدير"
                     else [k for k, v in perm_vars.items() if v.get()])
            salt = secrets.token_hex(16)
            with connect() as conn:
                conn.execute("INSERT INTO users(username,password_hash,role,active,created_at,permissions) "
                             "VALUES(?,?,?,?,?,?)",
                             (name, salt + "$" + hash_pwd(salt, p1), role, 1,
                              datetime.now().strftime("%Y-%m-%d %H:%M"),
                              json.dumps(perms, ensure_ascii=False)))
            # ★ تعديل ضروري معلن (إصدار 8 — الميزة 5): التفاصيل تذكر الدور المختار
            audit("إضافة مستخدم", f"{role}: {name}")      # ★ إضافة (ميزة 2)
            # ★ إضافة (إصدار 8 — الميزة 5): تسجيل الصلاحيات الممنوحة للمستخدم الجديد
            if role != "مدير":
                plabels = dict(PERMISSIONS)
                audit("تغيير صلاحيات", "مَنَح " + " و".join(f"«{plabels[k]}»" for k in perms)
                      + f" للمستخدم ({name})")
            messagebox.showinfo("تم", f"أُنشئ حساب {role} «{name}» بنجاح", parent=win)
            self.refresh_users()
            win.destroy()

        e_con.bind("<Return>", lambda e: do_add())
        self.mk_btn(card, "💾 حفظ", do_add, GREEN).pack(pady=12)

    def edit_permissions_dialog(self):
        """★ إضافة (إصدار 8 — الميزة 5): تعديل صلاحيات المستخدم المحدد — عشر
        صلاحيات بمربعات اختيار (دور «مدير» تظهر كلها مقفلة لأنه يملكها دائماً)،
        وكل منح/سحب يُسجل في سجل التدقيق: من أعطى/سحب ماذا ومن"""
        sel = self.tv_users.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر مستخدماً من الجدول أولاً"); return
        uid = int(sel[0])
        with connect() as conn:
            urow = conn.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
        if urow is None:
            return
        # ★ إضافة (إصدار 8 — الميزة 3): تسجيل النافذة في التتبع المركزي
        win = self.register_window(tk.Toplevel(self))
        win.title("تعديل الصلاحيات")
        win.geometry("520x660"); win.configure(bg=BG); win.resizable(False, False)
        card = tk.Frame(win, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=16)
        tk.Label(card, text="✏️ تعديل الصلاحيات", bg=CARD, fg=DARK, font=FT).pack(pady=(14, 2))
        tk.Label(card, text=f"المستخدم: {urow['username']} ({urow['role']})",
                 bg=CARD, fg=GRAY, font=("Segoe UI", 10)).pack(pady=(0, 8))
        is_mgr = (urow["role"] == "مدير")
        old_perms = load_user_permissions(urow["username"])
        perm_vars, perm_cbs = {}, {}
        for key, label in PERMISSIONS:
            v = tk.BooleanVar(value=(is_mgr or key in old_perms))
            cb = tk.Checkbutton(card, text=label, variable=v, font=F, bg=CARD,
                                fg=DARK, selectcolor="#dbeafe", activebackground=CARD,
                                activeforeground=ACCENT, anchor="e", justify="right",
                                onvalue=True, offvalue=False)
            cb.pack(fill="x", padx=30, pady=1)
            if is_mgr:                   # المدير: كل الصلاحيات مقفلة دائماً
                cb.config(state="disabled")
            perm_vars[key] = v
            perm_cbs[key] = cb
        tk.Label(card, text=("🔒 هذا الحساب مدير — يملك كل الصلاحيات دائماً (مقفلة)" if is_mgr
                             else "فعّل ما تريد منحه وألغِ ما تريد سحبه — كل تغيير يُسجل في سجل التدقيق"),
                 bg=CARD, fg=GRAY, font=("Segoe UI", 9)).pack(pady=(6, 0))

        def do_save_perms():
            new_perms = [k for k, v in perm_vars.items() if v.get()]
            if is_mgr:
                messagebox.showinfo("تنبيه", "المدير يملك كل الصلاحيات دائماً", parent=win)
                return
            plabels = dict(PERMISSIONS)
            granted = [k for k in new_perms if k not in old_perms]
            revoked = [k for k in old_perms if k not in new_perms]
            with connect() as conn:
                conn.execute("UPDATE users SET permissions=? WHERE id=?",
                             (json.dumps(new_perms, ensure_ascii=False), uid))
            for k in granted:            # سجل التدقيق: من أعطى/سحب ماذا ومن
                audit("تغيير صلاحيات", f"مَنَح «{plabels[k]}» للمستخدم ({urow['username']})")
            for k in revoked:
                audit("تغيير صلاحيات", f"سحب «{plabels[k]}» من المستخدم ({urow['username']})")
            messagebox.showinfo("تم", "تم حفظ صلاحيات المستخدم بنجاح", parent=win)
            self.refresh_users()
            win.destroy()

        self.mk_btn(card, "💾 حفظ الصلاحيات", do_save_perms, "#0d9488").pack(pady=12)

    def reset_password_dialog(self):
        """★ إضافة (إصدار 3 — ميزة 5): إعادة تعيين كلمة مرور أي مستخدم — للمدير فقط من هنا"""
        sel = self.tv_users.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر مستخدماً من الجدول أولاً"); return
        with connect() as conn:
            row = conn.execute("SELECT * FROM users WHERE id=?", (int(sel[0]),)).fetchone()
        if row is None:
            return
        # ★ إضافة (إصدار 8 — الميزة 3): تسجيل النافذة في التتبع المركزي
        win = self.register_window(tk.Toplevel(self))
        win.title("إعادة تعيين كلمة المرور")
        win.geometry("430x310"); win.configure(bg=BG); win.resizable(False, False)
        card = tk.Frame(win, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=16)
        tk.Label(card, text="🔑 إعادة تعيين كلمة المرور", bg=CARD, fg=DARK, font=FT).pack(pady=(14, 4))
        tk.Label(card, text=f"المستخدم: {row['username']} ({row['role']})", bg=CARD, fg=GRAY,
                 font=("Segoe UI", 10)).pack(pady=(0, 8))

        def frow(label):
            fr = tk.Frame(card, bg=CARD); fr.pack(fill="x", padx=18, pady=5)
            tk.Label(fr, text=label, bg=CARD, fg=DARK, font=FB, width=20, anchor="e").pack(side="right")
            e = tk.Entry(fr, font=F, justify="center", show="•", relief="solid", bd=1, width=22)
            e.pack(side="right", padx=(0, 8), ipady=4)
            return e

        e_pwd = frow("كلمة المرور الجديدة:")
        e_con = frow("تأكيد كلمة المرور:")

        def do_reset():
            p1, p2 = e_pwd.get(), e_con.get()
            if len(p1) < 4:
                messagebox.showwarning("تنبيه", "كلمة المرور قصيرة جداً (4 أحرف على الأقل)", parent=win); return
            if p1 != p2:
                messagebox.showwarning("تنبيه", "التأكيد لا يطابق كلمة المرور", parent=win); return
            salt = secrets.token_hex(16)
            with connect() as conn:
                conn.execute("UPDATE users SET password_hash=? WHERE id=?",
                             (salt + "$" + hash_pwd(salt, p1), row["id"]))
            audit("إعادة تعيين كلمة مرور", f"{row['username']} — بواسطة {self.user_name}")
            messagebox.showinfo("تم", f"أُعيد تعيين كلمة مرور «{row['username']}» بنجاح", parent=win)
            win.destroy()

        e_con.bind("<Return>", lambda e: do_reset())
        self.mk_btn(card, "💾 حفظ", do_reset, ACCENT).pack(pady=12)

    def toggle_user_active(self):
        """★ إضافة (إصدار 3 — ميزة 5): إيقاف/تفعيل حساب —
        ممنوع إيقاف نفسك، وممنوع إيقاف آخر مدير، ولا حذف نهائي حفاظاً على العمليات القديمة"""
        sel = self.tv_users.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر مستخدماً من الجدول أولاً"); return
        uid = int(sel[0])
        with connect() as conn:
            row = conn.execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
        if row is None:
            return
        if row["username"] == self.user_name:
            messagebox.showwarning("ممنوع", "لا يمكنك إيقاف حسابك نفسه"); return
        if not row["active"]:
            if not messagebox.askyesno("تأكيد", f"تفعيل حساب «{row['username']}» من جديد؟"):
                return
            with connect() as conn:
                conn.execute("UPDATE users SET active=1 WHERE id=?", (uid,))
            audit("تفعيل مستخدم", row["username"])
            messagebox.showinfo("تم", f"تم تفعيل حساب «{row['username']}»")
        else:
            if row["role"] == "مدير":
                with connect() as conn:
                    n = conn.execute("SELECT COUNT(*) FROM users WHERE role='مدير' AND active=1"
                                     ).fetchone()[0]
                if n <= 1:
                    messagebox.showwarning("ممنوع",
                        "لا يمكن إيقاف آخر مدير — يجب أن يبقى مدير مفعّل واحد على الأقل")
                    return
            if not messagebox.askyesno("تأكيد",
                    f"إيقاف حساب «{row['username']}»؟\nلن يستطيع تسجيل الدخول حتى يُفعّل من جديد."):
                return
            with connect() as conn:
                conn.execute("UPDATE users SET active=0 WHERE id=?", (uid,))
            audit("إيقاف مستخدم", row["username"])
            messagebox.showinfo("تم", f"تم إيقاف حساب «{row['username']}»")
        self.refresh_users()

    # ---------- (ميزة 6) شاشة تقرير أداء البائعين ----------
    def show_sellers(self):
        """★ إضافة (إصدار 3 — ميزة 6): فتح شاشة تقرير أداء البائعين — للمدير فقط"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «تقرير أداء البائعين» بدل «المدير فقط»
        if not self.require_admin("perf_report"):
            return
        self.show_page("sellers")

    def build_sellers_page(self, p):
        self.page_head(p, "📈 تقرير أداء البائعين",
                       "أداء كل بائع ضمن مدى تاريخ — عدد وقيمة المبيعات والمرتجعات والصافي")
        frow = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        frow.pack(fill="x", padx=25, pady=6)

        def date_cell(label):
            c = tk.Frame(frow, bg=CARD); c.pack(side="right", padx=10, pady=10)
            tk.Label(c, text=label, bg=CARD, fg=DARK, font=FB).pack(side="right")
            e = tk.Entry(c, font=F, justify="center", relief="solid", bd=1, width=13)
            e.pack(side="right", padx=(6, 0), ipady=4)
            return e

        self.e_perf_from = date_cell("من تاريخ:")
        self.e_perf_to   = date_cell("إلى تاريخ:")
        tk.Label(frow, text="الصيغ المقبولة: 2025-01-10 أو 10-01-2025 أو 10/01/2025",
                 bg=CARD, fg=GRAY, font=("Segoe UI", 9)).pack(side="right", padx=10)
        # ★ زر سريع «اليوم» يعبئ المدى بتاريخ اليوم ويعرض التقرير فوراً
        self.mk_btn(frow, "⚡ اليوم", self.sellers_range_today, ORANGE).pack(side="left", padx=6)
        self.mk_btn(frow, "🔍 عرض التقرير", self.run_sellers_report, ACCENT).pack(side="left", padx=10)

        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): الأعمدة تصبح
        # البائع | عدد العمليات | نقداً | شبكة | المرتجعات | الصافي
        frm, self.tv_sellers = self.mk_tree(p,
            ["الصافي", "المرتجعات", "شبكة", "نقداً", "عدد العمليات", "البائع"],
            [120, 120, 115, 115, 100, 160])
        frm.pack(fill="both", expand=True, padx=25, pady=8)

        # ★ الإجمالي التراكمي أسفل الجدول
        self.lbl_perf_total = tk.Label(p, text="", bg=BG, fg=ACCENT, font=FB)
        self.lbl_perf_total.pack(fill="x", padx=25)

        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25, pady=(0, 18))
        self.mk_btn(bar, "📊 تصدير التقرير Excel", self.export_sellers_xlsx, "#0d9488").pack(side="right", padx=6)

        self.sellers_report_rows = []     # آخر تقرير معروض (يُستخدم للتصدير)
        self.sellers_report_total = []    # صف الإجمالي التراكمي

    def sellers_range_today(self):
        """★ إضافة (إصدار 3 — ميزة 6): زر سريع يعبئ المدى بتاريخ اليوم ويعرض التقرير"""
        t = today_str()
        self.e_perf_from.delete(0, "end"); self.e_perf_from.insert(0, t)
        self.e_perf_to.delete(0, "end");   self.e_perf_to.insert(0, t)
        self.run_sellers_report()

    def run_sellers_report(self):
        """★ إضافة (إصدار 3 — ميزة 6): تقرير أداء البائعين ضمن المدى + الإجمالي التراكمي"""
        f, t = parse_date_multi(self.e_perf_from.get()), parse_date_multi(self.e_perf_to.get())
        bad = [lbl for lbl, v in (("من تاريخ", f), ("إلى تاريخ", t)) if v is None]
        if bad:
            messagebox.showwarning("تاريخ خاطئ",
                "صيغة غير صحيحة لـ " + " و ".join(bad) +
                "\nالصيغ المقبولة: 2025-01-10 أو 10-01-2025 أو 10/01/2025")
            return
        sql = "SELECT seller_name, type, COUNT(*), SUM(total) FROM operations"
        cond, params = [], []
        if f:
            cond.append("date >= ?"); params.append(f)
        if t:
            cond.append("date <= ?"); params.append(t)
        if cond:
            sql += " WHERE " + " AND ".join(cond)
        sql += " GROUP BY seller_name, type"
        agg = {}
        with connect() as conn:
            for seller, typ, cnt, sm in conn.execute(sql, params):
                # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): تجميع عدد العمليات
                # مع فصل نقداً عن شبكة (والمرتجعات كما كانت مخزنة سالبة فتُعرض موجبة)
                a = agg.setdefault(seller or "غير محدد",
                                   {"n": 0, "cash": 0.0, "netw": 0.0, "rv": 0.0})
                a["n"] += cnt
                if typ == "مرتجع":
                    a["rv"] += -(sm or 0)
                elif typ == "شبكة":
                    a["netw"] += (sm or 0)
                else:              # نقداً (وقيم المبيع القديمة بعد الترقية)
                    a["cash"] += (sm or 0)
        self.tv_sellers.delete(*self.tv_sellers.get_children())
        self.sellers_report_total = []
        rows = []
        for seller, a in sorted(agg.items(),
                                key=lambda kv: (kv[1]["cash"] + kv[1]["netw"] - kv[1]["rv"]),
                                reverse=True):
            net = a["cash"] + a["netw"] - a["rv"]
            rows.append([round(net, 2), round(a["rv"], 2), round(a["netw"], 2),
                         round(a["cash"], 2), a["n"], seller])
        for r in rows:
            self.tv_sellers.insert("", "end", values=(money(r[0]), money(r[1]), money(r[2]),
                                                      money(r[3]), r[4], r[5]))
        if not rows:
            self.lbl_perf_total.config(text="لا توجد عمليات في هذا المدى", fg=GRAY)
        else:
            # ★ تعديل (إصدار 5): صف الإجمالي التراكمي بنفس الأعمدة الجديدة
            tn, tcash = sum(r[4] for r in rows), sum(r[3] for r in rows)
            tnetw, trv = sum(r[2] for r in rows), sum(r[1] for r in rows)
            tnet = tcash + tnetw - trv
            self.lbl_perf_total.config(
                text=(f"الإجمالي — {tn} عملية — نقداً: {money(tcash)} — شبكة: {money(tnetw)} — "
                      f"المرتجعات: {money(trv)} — الصافي: {money(tnet)}"),
                fg=(GREEN if tnet >= 0 else RED))
            self.sellers_report_total = [round(tnet, 2), round(trv, 2), round(tnetw, 2),
                                         round(tcash, 2), tn, "الإجمالي"]
        self.sellers_report_rows = rows

    def export_sellers_xlsx(self):
        """★ إضافة (إصدار 3 — ميزة 6): تصدير تقرير أداء البائعين إلى Excel بنفس export_xlsx"""
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «تصدير التقارير (CSV/Excel/PDF)»
        if not self.has_permission("export_reports"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «تصدير التقارير»")
            return
        if not self.sellers_report_rows:
            messagebox.showinfo("تنبيه", "اعرض التقرير أولاً (حدد المدى ثم اضغط «عرض التقرير»)")
            return
        path = filedialog.asksaveasfilename(title="حفظ تقرير البائعين", defaultextension=".xlsx",
                                            initialfile=f"أداء_البائعين_{today_str()}.xlsx",
                                            filetypes=[("ملف Excel", "*.xlsx")])
        if not path:
            return
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): نفس الأعمدة الجديدة
        # البائع | عدد العمليات | نقداً | شبكة | المرتجعات | الصافي
        headers = ["البائع", "عدد العمليات", "نقداً", "شبكة", "المرتجعات", "الصافي"]
        widths  = [20, 12, 14, 14, 14, 14]
        # ترتيب الأعمدة في Excel معكوس عن الجدول (الورقة RTL: العمود الأول يظهر أقصى اليمين)
        rows = [[r[5], r[4], r[3], r[2], r[1], r[0]] for r in self.sellers_report_rows]
        if self.sellers_report_total:
            tt = self.sellers_report_total
            rows.append([tt[5], tt[4], tt[3], tt[2], tt[1], tt[0]])
        export_xlsx(path, headers, rows, widths,
                    desc=f"تقرير أداء البائعين — {len(self.sellers_report_rows)} بائعاً")
        messagebox.showinfo("تم", "تم تصدير تقرير البائعين إلى Excel ✅")

    # ═══════════════════════════════════════════════════════════
    # ★★★ إضافات الإصدار 4 — تبديل المستخدم ولوحة المعلومات ★★★
    # ═══════════════════════════════════════════════════════════

    # ---------- (ميزة 1) تبديل المستخدم دون إغلاق البرنامج ----------
    def login_dialog(self):
        """★ إضافة (إصدار 4 — ميزة 1): شاشة تسجيل الدخول الحالية بتصميمها وسلوكها
        نفسه تماماً (نفس الرسائل الثلاث ونفس سجل التدقيق ونمط الحقول والأزرار)
        — تُعرض كنافذة Toplevel فوق النافذة الرئيسية المخفية عند تبديل المستخدم.
        سبب عدم استدعاء login_flow نفسها: هي تنشئ نافذة Tk ثانية وتشغّل mainloop
        خاصاً بها، وحلقة الأحداث المتداخلة لنافذة Tk ثانية لا تعود أبداً بعد
        تدميرها ما دامت النافذة الرئيسية حية (تُعلّق البرنامج كلياً)، بينما
        wait_window لنافذة Toplevel هي الطريقة القياسية الآمنة للحواريات.
        ★ تعديل مصرح به (إصدار 9): نفس إعادة بناء نافذة الدخول المصرح بها في
        login_flow — البناء كله انتقل لـ _screen_login_build المشتركة بنفس
        المنطق حرفياً وبنفس الميزات الثماني (التعديل المصرح به الوحيد)"""
        result = {"name": None, "role": None}
        win = tk.Toplevel(self)
        _screen_login_build(win, result)
        win.protocol("WM_DELETE_WINDOW", win.destroy)
        win.wait_window(win)          # حلقة أحداث محلية آمنة — تعود فور إغلاق النافذة
        return result if result["role"] else None

    def switch_user(self):
        """★ إضافة (إصدار 4 — ميزة 1): تبديل المستخدم دون إغلاق البرنامج —
        تحذير إذا كانت السلة فيها أصناف، تسجيل الخروج في سجل التدقيق، إخفاء
        النافذة الرئيسية وإظهار نافذة تسجيل الدخول الحالية من جديد، وعند نجاح
        الدخول تُصفَّر الجلسة وتتكيف كل الشاشات مع صلاحيات المستخدم الجديد.
        إلغاء الدخول يغلق البرنامج بأمان (كما عند بدء التشغيل)"""
        # تحذير: السلة فيها أصناف ستُفقد عند التبديل
        if getattr(self, "cart", None):
            if not messagebox.askyesno("تبديل المستخدم",
                    "السلة فيها أصناف ستُفقد عند التبديل — متابعة؟"):
                return
        # ★ إضافة (إصدار 8 — الميزة 3): أول خطوة قبل إظهار نافذة الدخول — إغلاق
        # كل النوافذ المفتوحة فوراً (تفاصيل اليوم، المعاينة، إدارة المستخدمين،
        # تغيير كلمة المرور...) مع إفراغ السلة (تحذير السلة الحالي أعلاه باقٍ
        # كما هو) — فلا تبقى أي شاشة تعمل باسم المستخدم القديم بعد التبديل أبداً
        closed_count = self.close_all_windows()
        audit(f"تبديل مستخدم — إغلاق {closed_count} نافذة مفتوحة")
        audit("تبديل مستخدم — خروج " + self.user_name)   # تسجيل الخروج في سجل التدقيق
        self.withdraw()                    # إخفاء النافذة الرئيسية
        try:
            # ★ تعديل ضروري معلن (إصدار 4 — ميزة 1): شاشة الدخول نفسها تُعرض عبر
            # login_dialog (Toplevel + wait_window) بدل استدعاء login_flow مباشرة —
            # لأن login_flow تنشئ نافذة Tk ثانية بـ mainloop خاص لا يعود أبداً بعد
            # تدميرها ما دامت النافذة الرئيسية حية (يُعلّق البرنامج كلياً)،
            # والبديل يعطي نفس الشاشة ونفس السلوك ونفس سجل التدقيق تماماً
            session = self.login_dialog()  # شاشة تسجيل الدخول من جديد
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            session = None
        if session is None:
            self.exit_app()                # أُلغي الدخول: إغلاق آمن كما عند بدء التشغيل
            return
        # نجاح الدخول: تصفير الجلسة للمستخدم الجديد
        CURRENT_USER["name"] = session["name"]
        self.user_name = session["name"]
        self.role = session["role"]
        self.user_role = session["role"]
        # ★ إضافة (إصلاح 1 — بعد تبديل المستخدم): الجلسة الجديدة تبدأ بلا
        # إخفاء سابق للشريط (حتى يظهر للمستخدم الجديد إن وُجد تحديث)، مع
        # فحص صامت واحد بعد الدخول بنفس دالة الفحص القائمة نفسها — كما
        # بعد الدخول عند بدء التشغيل تماماً
        self.update_bar_dismissed = False
        self.update_bar_dismissed_version = None
        self.after(1200, lambda: update_check_silent(self))
        self.cart = []                     # السلة تُفرغ
        if hasattr(self, "e_inv_customer"):
            self.e_inv_customer.delete(0, "end")
        if hasattr(self, "lbl_inv_status"):
            self.lbl_inv_status.config(text="")
        self.update_cart_view()
        if hasattr(self, "cb_today_filter"):      # تصفير فلاتر عمليات اليوم
            self.cb_today_filter.set("الكل")
        if getattr(self, "today_type_var", None) is not None:
            self.today_type_var.set("الكل")
        if hasattr(self, "e_search"):             # مسح نتائج بحث المستخدم السابق
            self.e_search.delete(0, "end")
        if hasattr(self, "tv_search"):
            self.tv_search.delete(*self.tv_search.get_children())
            self.lbl_search.config(text="")
        for attr in ("tv_audit", "tv_users", "tv_sellers"):   # مسح شاشات المدير
            tv = getattr(self, attr, None)
            if tv is not None:
                tv.delete(*tv.get_children())
        if hasattr(self, "lbl_perf_total"):
            self.lbl_perf_total.config(text="")
            self.sellers_report_rows = []
            self.sellers_report_total = []
        for v in getattr(self, "dash_cards", {}).values():     # مسح لوحة المعلومات
            v.config(text="—")
        if hasattr(self, "tv_dash_items"):
            self.tv_dash_items.delete(*self.tv_dash_items.get_children())
        if hasattr(self, "lbl_dash_range"):
            self.lbl_dash_range.config(text="")
        if hasattr(self, "lbl_chart_info"):
            self.lbl_chart_info.config(
                text="📈 صافي آخر 30 يوم عمل — مرّر المؤشر فوق أي عمود لعرض قيمته", fg=GRAY)
        self.apply_role_ui()               # تكييف الشريط الجانبي والشاشات مع الدور
        self.show_page("new")              # العودة لصفحة «عملية جديدة» (تحدّث الشريط العلوي)
        self.refresh_today()               # تحديث عمليات اليوم
        self.refresh_archive()             # تحديث الأرشيف
        self.deiconify()                   # إعادة إظهار النافذة الرئيسية

    def apply_role_ui(self):
        """★ إضافة (إصدار 4 — ميزة 1): تكييف الواجهة مع دور المستخدم الحالي بعد
        التبديل — إظهار/إخفاء أزرار المدير وملاحظات البائع وفلتر البائع وتحديث
        اسم المستخدم تحت الشعار (الشريط العلوي والأرشيف الإجمالي يبقيان عامين كما هما)"""
        self.lbl_user.config(text=f"👤 {self.user_name} ({self.role})")
        if self.role == "مدير":
            for b in self.manager_btns:       # أزرار المدير تظهر
                b.pack(fill="x", padx=10, pady=3)
            self.lbl_today_only.pack_forget()
            self.fr_today_filter.pack(side="left", padx=12)
            if hasattr(self, "lbl_search_only"):
                self.lbl_search_only.pack_forget()
        else:
            for b in self.manager_btns:       # أزرار المدير تختفي عن البائع
                b.pack_forget()
            self.fr_today_filter.pack_forget()
            self.lbl_today_only.pack(side="left", padx=12)
            if hasattr(self, "lbl_search_only"):
                self.lbl_search_only.pack(fill="x", padx=25, anchor="e")

        # ★ إضافة (إصدار 8 — الميزة 5+6+7): إعادة بناء ظهور أزرار الشريط
        # الجانبي حسب صلاحيات المستخدم الجديد الفعلية عند كل دخول/تبديل
        # (المدير يملك كل الصلاحيات دائماً — والبائع بحسب ما مُنح له) +
        # تحديث نص زر قائمة المستخدم أسفل الشريط
        self.refresh_sidebar_permissions()
        # ★ إضافة (إصدار 10): مواءمة شريط إشعار التحديث مع دور المستخدم بعد
        # التبديل — البائع يرى «راجع المدير» والمدير يرى زر «تحديث الآن»
        self.refresh_update_bar()

    # ---------- (ميزة 5) تلميحات Tooltip على كل الأزرار ----------
    def attach_button_tips(self):
        """★ إضافة (إصدار 4 — ميزة 5): تلميحات عربية على أزرار الشريط الجانبي
        وأزرار العمل — تُربط بالبحث عن نص الزر دون أي تعديل في مواضع إنشائها"""
        btn_tips = {
            # أزرار الشريط الجانبي
            "➕  عملية جديدة": "إدخال عملية جديدة (نقداً/شبكة/مرتجع) على تاريخ اليوم",
            "📋  عمليات اليوم": "عرض عمليات اليوم الحالي وإدارتها",
            "🗂️  الأرشيف والتقارير": "تقارير الأيام المغلقة مع التصفية والتصدير",
            "🔎  بحث": "بحث جزئي عن صنف في كل العمليات",
            "🧾  فاتورة أصناف": "تجميع عدة أصناف في سلة وحفظها دفعة واحدة",
            "📊  لوحة المعلومات": "ملخص شامل وإحصائيات ورسم بياني — للمدير فقط",
            "👥  إدارة المستخدمين": "إضافة البائعين وإدارة حساباتهم — للمدير فقط",
            "📜  سجل التدقيق": "سجل كل الإجراءات — للمدير فقط",
            "📈  تقرير أداء البائعين": "أداء كل بائع ضمن مدى تاريخ — للمدير فقط",
            "🔄 تبديل المستخدم": "تسجيل الخروج والدخول بحساب آخر دون إغلاق البرنامج",
            "💾 نسخة احتياطية الآن": "إنشاء نسخة احتياطية من قاعدة البيانات فوراً",
            "🔑 تغيير كلمة المرور": "تغيير كلمة مرور حسابك الحالي",
            "⏻  خروج": "إغلاق البرنامج مع نسخة احتياطية تلقائية",
            # أزرار العمل
            "💾  حفظ العملية": "حفظ العملية الحالية على تاريخ اليوم",
            "🔄 تحديث": "تحديث البيانات المعروضة من قاعدة البيانات",
            "➕ إضافة إلى السلة": "إضافة الصنف الحالي إلى سلة الفاتورة (أو Enter)",
            "🗑 إزالة المحدد من السلة": "إزالة الصنف المحدد من السلة قبل الحفظ",
            "💾 حفظ الفاتورة كاملة": "حفظ كل أصناف السلة دفعة واحدة كعمليات اليوم",
            "🔒 إغلاق اليوم وحفظ التقرير": "إنهاء اليوم وحفظ تقريره في الأرشيف — للمدير فقط",
            "🗑 حذف العملية المحددة": "حذف العملية المحددة من جدول اليوم — للمدير فقط",
            "🔓 إعادة فتح اليوم": "حذف تقرير اليوم المحدد للسماح بالإضافة من جديد — للمدير فقط",
            "📊 تصدير الأرشيف كاملاً Excel": "تصدير كل تقارير الأرشيف إلى ملف Excel",
            "📥 تصدير اليوم إلى CSV": "تصدير عمليات اليوم المحدد إلى ملف CSV",
            "📄 عرض تفاصيل اليوم": "عرض تفاصيل اليوم المحدد (أو نقر مزدوج على الصف)",
            "🔍 تصفية": "تصفية الأرشيف ضمن مدى التاريخ المُدخل",
            "↩ عرض الكل": "مسح التصفية وعرض كل التقارير",
            "بحث": "ابحث عن الصنف في كل العمليات (أو Enter)",
            "⚡ اليوم": "عرض تقرير اليوم الحالي فقط",
            "🔍 عرض التقرير": "عرض تقرير الأداء ضمن المدى المُدخل",
            "📊 تصدير التقرير Excel": "تصدير تقرير الأداء المعروض إلى Excel",
            "🚫 إيقاف / تفعيل": "إيقاف الحساب المحدد أو تفعيله من جديد",
            "🔑 إعادة تعيين كلمة المرور": "تعيين كلمة مرور جديدة للمستخدم المحدد",
            "➕ إضافة بائع": "إنشاء حساب بائع جديد",
            # ★ إضافة (إصدار 8 — الميزة 1+5): تلميحات الأزرار الجديدة والمُحدّثة
            "➕ إضافة مستخدم": "إنشاء حساب جديد (بائع أو مدير) مع تحديد صلاحياته",
            "✏️ تعديل الصلاحيات": "تعديل صلاحيات المستخدم المحدد — كل منح أو سحب يُسجل في سجل التدقيق",
            "👁 عرض الكل": "إعادة سجل التدقيق كاملاً وإلغاء الفلتر النشط",
            "⚙️ الإجراءات": "قائمة بكل إجراءات اليوم المحدد: عرض، طباعة، تصدير، إعادة فتح",
        }
        # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): التلميحات تذكر الأنواع الثلاثة
        radio_tips = {"نقداً": "نوع العملية: نقداً — الدرج النقدي (قيمة موجبة)",
                      "شبكة": "نوع العملية: شبكة — جهاز الشبكة (قيمة موجبة)",
                      "مرتجع": "نوع العملية: مرتجع (قيمة سالبة تُخصم من الإجمالي)"}
        skip = getattr(self, "fr_today_type", None)   # فلتر النوع له تلميحاته الخاصة
        def walk(w):
            try:
                txt = w.cget("text")
            except Exception:
                txt = ""
            if isinstance(w, tk.Button) and txt in btn_tips:
                add_tip(w, btn_tips[txt])
            elif (isinstance(w, tk.Radiobutton) and txt in radio_tips
                  and (skip is None or w.master is not skip)):
                add_tip(w, radio_tips[txt])
            for ch in w.winfo_children():
                walk(ch)
        walk(self)
        if hasattr(self, "cb_today_filter"):        # فلتر البائع للمدير
            add_tip(self.cb_today_filter, "فلترة عمليات اليوم حسب البائع")

    # ---------- (ميزة 2+3) لوحة المعلومات والرسم البياني ----------
    def show_dashboard(self):
        """★ إضافة (إصدار 4 — ميزة 2): فتح لوحة المعلومات — للمدير فقط"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «لوحة المعلومات» بدل «المدير فقط»
        if not self.require_admin("dashboard"):
            return
        self.show_page("dash")
        self.refresh_dashboard()

    def build_dashboard_page(self, p):
        """★ إضافة (إصدار 4 — ميزة 2): لوحة معلومات شاملة — أزرار فترة سريعة،
        6 بطاقات (أيام العمل/المبيعات/المرتجعات/الصافي + أعلى يوم + المتوسط)،
        جدول أفضل 5 أصناف، والرسم البياني (الميزة 3) أسفل الشاشة — كلها من
        جداول operations و daily_reports باستعلامات جديدة فقط"""
        self.page_head(p, "📊 لوحة المعلومات",
                       "ملخص شامل للفترة المختارة — للمدير فقط")

        # صف أزرار الفترة السريعة: آخر 30 يوم / هذا الشهر / الشهر الماضي / الكل
        prow = tk.Frame(p, bg=BG); prow.pack(fill="x", padx=25, pady=(0, 4))
        self.dash_period = "last30"
        self.dash_period_colors = {"last30": ACCENT, "month": GREEN,
                                   "prevmonth": ORANGE, "all": "#475569"}
        period_tips = {"last30": "عرض بيانات آخر 30 يوماً",
                       "month": "عرض بيانات الشهر الحالي",
                       "prevmonth": "عرض بيانات الشهر الماضي",
                       "all": "عرض كل البيانات منذ البداية"}
        self.dash_period_btns = {}
        for key, label in [("last30", "🗓 آخر 30 يوم"), ("month", "📅 هذا الشهر"),
                           ("prevmonth", "📆 الشهر الماضي"), ("all", "🗃 الكل")]:
            b = self.mk_btn(prow, label, lambda k=key: self.set_dash_period(k),
                            self.dash_period_colors[key])
            b.pack(side="right", padx=4)
            if key != self.dash_period:      # إبراز زر الفترة المختارة
                b.config(bg="#64748b", activebackground="#64748b")
            add_tip(b, period_tips[key])     # ★ (إصدار 4 — ميزة 5): تلميح الفترة
            self.dash_period_btns[key] = b
        self.lbl_dash_range = tk.Label(p, text="", bg=BG, fg=GRAY,
                                       font=("Segoe UI", 10, "bold"))
        self.lbl_dash_range.pack(fill="x", padx=25, anchor="e")

        # بطاقات الفترة: عدد أيام العمل والمبيعات والمرتجعات والصافي الكلي،
        # ثم بطاقتا أعلى يوم إيراداً ومتوسط الإيراد اليومي
        cards = tk.Frame(p, bg=BG); cards.pack(fill="x", padx=25, pady=4)
        self.dash_cards = {}
        for title, color in [("عدد أيام العمل", "#334155"), ("إجمالي المبيعات", GREEN),
                             ("إجمالي المرتجعات", RED), ("الصافي الكلي", ACCENT),
                             ("أعلى يوم إيراداً", "#7c3aed"),
                             ("متوسط الإيراد اليومي", "#0d9488")]:
            fr, v = self.mk_card(cards, title, color)
            fr.pack(side="right", expand=True, fill="x", padx=5)
            self.dash_cards[title] = v

        # ★ إضافة (إصدار 5 — نظام الأنواع الثلاثة): بطاقتان صغيرتان تفصلان مبيعات
        # الدرج النقدي عن مبيعات جهاز الشبكة للفترة المختارة — «إجمالي المبيعات"
        # أعلاه يبقى نقداً + شبكة مجتمعين كما هو
        row2 = tk.Frame(p, bg=BG); row2.pack(fill="x", padx=25, pady=(0, 4))
        for title, color in [("مبيعات نقداً", GREEN), ("مبيعات شبكة", ACCENT)]:
            fr, v = self.mk_card(row2, title, color)
            fr.pack(side="right", padx=5, ipadx=26)
            self.dash_cards[title] = v

        # جدول أفضل 5 أصناف في الفترة: الصنف | الكمية المبيعة | عدد المرات | قيمة المبيعات
        tk.Label(p, text="🏆 أفضل 5 أصناف في الفترة", bg=BG, fg=DARK,
                 font=("Segoe UI", 11, "bold")).pack(fill="x", padx=25, anchor="e")
        frm, self.tv_dash_items = self.mk_tree(p,
            ["قيمة المبيعات", "عدد المرات", "الكمية المبيعة", "الصنف"],
            [130, 100, 120, 240])
        frm.pack(fill="both", expand=True, padx=25, pady=(2, 4))
        self._chart_bars = []

        # (ميزة 3) الرسم البياني أسفل الشاشة — tk.Canvas فقط قابل للتمدد مع النافذة
        self.lbl_chart_info = tk.Label(
            p, bg=BG, fg=GRAY, font=("Segoe UI", 10, "bold"),
            text="📈 صافي آخر 30 يوم عمل — مرّر المؤشر فوق أي عمود لعرض قيمته")
        self.lbl_chart_info.pack(fill="x", padx=25, anchor="e")
        self.chart_canvas = tk.Canvas(p, bg="white", height=210,
                                      highlightbackground=BORDER, highlightthickness=1)
        self.chart_canvas.pack(fill="x", padx=25, pady=(2, 18))
        self.chart_canvas.bind("<Configure>", lambda e: self.draw_net_chart())
        self.chart_canvas.bind("<Motion>", self._chart_hover)
        self.chart_canvas.bind("<Leave>", lambda e: self.lbl_chart_info.config(
            text="📈 صافي آخر 30 يوم عمل — مرّر المؤشر فوق أي عمود لعرض قيمته",
            fg=GRAY))

    def set_dash_period(self, key):
        """★ إضافة (إصدار 4 — ميزة 2): اختيار فترة لوحة المعلومات وإبراز زرها"""
        self.dash_period = key
        for k, b in self.dash_period_btns.items():
            col = self.dash_period_colors[k] if k == key else "#64748b"
            b.config(bg=col, activebackground=col)
        self.refresh_dashboard()

    def refresh_dashboard(self):
        """★ إضافة (إصدار 4 — ميزة 2): حساب بطاقات لوحة المعلومات للفترة المختارة —
        استعلامات SQL جديدة فقط على الجداول الموجودة دون تعديل أي استعلام قائم"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): فحص الصلاحية الدقيقة بدل «المدير فقط»
        if not self.has_permission("dashboard"):
            return
        t = date.today()
        key = getattr(self, "dash_period", "last30")
        if key == "month":                     # هذا الشهر
            dfrom = t.replace(day=1).isoformat(); dto = t.isoformat(); name = "هذا الشهر"
        elif key == "prevmonth":               # الشهر الماضي
            last_prev = date.fromordinal(t.replace(day=1).toordinal() - 1)
            dfrom = last_prev.replace(day=1).isoformat(); dto = last_prev.isoformat()
            name = "الشهر الماضي"
        elif key == "all":                     # الكل
            dfrom = dto = ""; name = "الكل"
        else:                                  # آخر 30 يوم (الافتراضي)
            dfrom = date.fromordinal(t.toordinal() - 29).isoformat()
            dto = t.isoformat(); name = "آخر 30 يوم"
        self.lbl_dash_range.config(
            text="الفترة: " + name + (f" — من {dfrom} إلى {dto}" if dfrom else " — كل البيانات"))
        cond, params = [], []
        if dfrom:
            cond.append("date >= ?"); params.append(dfrom)
        if dto:
            cond.append("date <= ?"); params.append(dto)
        where = (" WHERE " + " AND ".join(cond)) if cond else ""
        with connect() as conn:
            # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): مقارنات النوع أصبحت
            # «نقداً» و«شبكة» بدل «بيع» — مع بطاقتي الفصل الجديدتين
            days, sales, rets, net, cashv, netwv = conn.execute(
                "SELECT COUNT(DISTINCT date),"
                " COALESCE(SUM(CASE WHEN type IN ('نقداً','شبكة') THEN total ELSE 0 END), 0),"
                " COALESCE(-SUM(CASE WHEN type='مرتجع' THEN total ELSE 0 END), 0),"
                " COALESCE(SUM(total), 0),"
                " COALESCE(SUM(CASE WHEN type='نقداً' THEN total ELSE 0 END), 0),"
                " COALESCE(SUM(CASE WHEN type='شبكة' THEN total ELSE 0 END), 0)"
                " FROM operations" + where, params).fetchone()
            top = conn.execute("SELECT date, SUM(total) FROM operations" + where +
                               " GROUP BY date ORDER BY SUM(total) DESC LIMIT 1",
                               params).fetchone()
            icond = ["type IN ('نقداً','شبكة')"] + cond   # ★ تعديل (إصدار 5): أفضل الأصناف من المبيعات (نقداً + شبكة) فقط
            items = conn.execute("SELECT item_name, SUM(quantity), COUNT(*), SUM(total)"
                                 " FROM operations WHERE " + " AND ".join(icond) +
                                 " GROUP BY item_name ORDER BY SUM(total) DESC LIMIT 5",
                                 params).fetchall()
        self.dash_cards["عدد أيام العمل"].config(text=str(days))
        self.dash_cards["إجمالي المبيعات"].config(text=money(sales))
        self.dash_cards["إجمالي المرتجعات"].config(text=money(rets))
        self.dash_cards["الصافي الكلي"].config(text=money(net),
                                               fg=(GREEN if net >= 0 else RED))
        # ★ إضافة (إصدار 5): بطاقتا فصل الدرج النقدي عن جهاز الشبكة للفترة المختارة
        self.dash_cards["مبيعات نقداً"].config(text=money(cashv))
        self.dash_cards["مبيعات شبكة"].config(text=money(netwv))
        if top is not None and top[1] is not None:
            self.dash_cards["أعلى يوم إيراداً"].config(text=f"{top[0]}\n{money(top[1])}")
        else:
            self.dash_cards["أعلى يوم إيراداً"].config(text="—")
        self.dash_cards["متوسط الإيراد اليومي"].config(
            text=(money(net / days) if days else "—"))
        self.tv_dash_items.delete(*self.tv_dash_items.get_children())
        for it in items:
            self.tv_dash_items.insert("", "end", values=(
                money(it[3] or 0), it[2], f"{it[1]:g}", it[0]))
        self.draw_net_chart()                  # (ميزة 3) تحديث الرسم مع اللوحة

    def draw_net_chart(self):
        """★ إضافة (إصدار 4 — ميزة 3): رسم أعمدة صافي آخر 30 يوم عمل من جدول
        daily_reports بـ tk.Canvas فقط (بلا أي مكتبة خارجية) — أخضر للموجب،
        أحمر للسالب، وعمود برتقالي منفصل لليوم الجاري إن لم يُغلق بعد،
        بارتفاع نسبي لأعلى قيمة وخط أرضي صفر — ولا يسبب أي خطأ مهما حدث"""
        cv = getattr(self, "chart_canvas", None)
        if cv is None:
            return
        try:
            cv.delete("all")
            w = max(cv.winfo_width(), 200)
            h = max(cv.winfo_height(), 150)
            # آخر 30 يوم عمل مغلق من جدول daily_reports
            with connect() as conn:
                rows = conn.execute("SELECT report_date, net_total FROM daily_reports "
                                    "ORDER BY report_date DESC LIMIT 30").fetchall()
            rows = [tuple(r) for r in reversed(rows)]
            # اليوم الجاري غير المغلق: عمود منفصل بالبرتقالي إن كانت له عمليات
            t = today_str()
            if not is_closed(t):
                # ★ تعديل (إصدار 5 — نظام الأنواع الثلاثة): day_totals ترجع الآن
                # (عدد العمليات، نقداً، شبكة، المرتجعات، الإجمالي)
                n0, _c, _n, _r, tnet = day_totals(t)
                if n0 > 0:
                    rows.append((t, tnet))
            self._chart_bars = []
            if not rows:
                cv.create_text(w // 2, h // 2, text="لا توجد بيانات لعرضها بعد",
                               fill=GRAY, font=("Segoe UI", 12, "bold"))
                return
            n = len(rows)
            vals = [(r[1] or 0) for r in rows]
            max_pos = max(max(vals), 0.0)
            max_neg = -min(min(vals), 0.0)
            top_pad, bottom_pad, side_pad = 26, 34, 14
            plot_h = max(h - top_pad - bottom_pad, 40)
            span = (max_pos + max_neg) or 1.0
            scale = plot_h / span                 # ارتفاع الأعمدة نسبي لأعلى قيمة
            zero_y = top_pad + max_pos * scale    # خط الأرض الصفري
            step = (w - 2 * side_pad) / n
            bw = max(step * 0.62, 3)
            for i, (dt, val) in enumerate(rows):
                v = val or 0
                x1 = side_pad + i * step + (step - bw) / 2
                x2 = x1 + bw
                is_open_today = (i == n - 1 and dt == today_str() and not is_closed(dt))
                color = ORANGE if is_open_today else (GREEN if v >= 0 else RED)
                y1 = zero_y - v * scale if v >= 0 else zero_y
                y2 = zero_y if v >= 0 else zero_y + (-v) * scale
                cv.create_rectangle(x1, y1, x2, y2, fill=color, width=0)
                if bw >= 34:                      # القيم على الأعمدة عند اتساع المساحة فقط
                    cv.create_text((x1 + x2) / 2, (y1 - 8 if v >= 0 else y2 + 8),
                                   text=f"{abs(v):,.0f}",
                                   fill=(DARK if v >= 0 else RED), font=("Segoe UI", 8))
                self._chart_bars.append((x1, x2, dt, v, is_open_today))
            # خط الأرض الصفري
            cv.create_line(side_pad, zero_y, w - side_pad, zero_y, fill=DARK, width=1)
            cv.create_text(side_pad + 4, zero_y - 9, text="0", fill=GRAY,
                           font=("Segoe UI", 8), anchor="w")
            # التواريخ تحت الأعمدة بصيغة يوم/شهر مبسطة وبلا ازدحام
            every = 1
            while every * step < 34 and every < n:
                every += 1
            for i in range(n):
                if i % every == 0 or i == n - 1:
                    dt = rows[i][0]
                    cv.create_text(side_pad + i * step + step / 2, h - 12,
                                   text=f"{int(dt[8:10])}/{int(dt[5:7])}",
                                   fill=GRAY, font=("Segoe UI", 8))
        except Exception:
            pass                    # الرسم لا يسبب أي خطأ أبداً

    def _chart_hover(self, e):
        """★ إضافة (إصدار 4 — ميزة 3): عرض قيمة العمود الذي يقف عليه المؤشر"""
        try:
            for x1, x2, dt, v, is_open in getattr(self, "_chart_bars", []):
                if x1 <= e.x <= x2:
                    self.lbl_chart_info.config(
                        text=f"📅 {dt} ({day_name(dt)}): {money(v)}"
                             + (" — اليوم الجاري ولم يُغلق بعد" if is_open else ""),
                        fg=(ORANGE if is_open else (GREEN if v >= 0 else RED)))
                    return
        except Exception:
            pass

    # ═══════════════════════════════════════════════════════════
    # ★★★ إضافات الإصدار 6 — الطباعة الحرارية داخل التطبيق ★★★
    # ═══════════════════════════════════════════════════════════

    # ---------- (3) شاشة إعدادات الطباعة — للمدير فقط ----------
    def show_print_settings(self):
        """★ إضافة (إصدار 6): فتح شاشة إعدادات الطباعة — للمدير فقط"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «إعدادات الطباعة» بدل «المدير فقط»
        if not self.require_admin("print_settings"):
            return
        self.show_page("print")
        self.refresh_printer_list()

    def build_print_settings_page(self, p):
        """★ إضافة (إصدار 6): شاشة إعدادات الطباعة — قائمة طابعات ويندوز
        المثبتة + زر تحديث القائمة + طباعة تجريبية + اسم المحل + خيار
        الطباعة التلقائية عند الإغلاق، وكلها تُحفظ في جدول settings الموجود
        (المفاتيح: printer_name / store_name / auto_print_daily)"""
        self.page_head(p, "⚙️ إعدادات الطباعة",
                       "الطباعة الحرارية لتقارير اليوم (Epson TM-T20III — ورق 80mm) — للمدير فقط")

        # بطاقة اختيار الطابعة: قائمة ويندوز المنسدلة + تحديث + طباعة تجريبية
        card1 = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card1.pack(fill="x", padx=25, pady=8)
        tk.Label(card1, text="🖨 الطابعة الحرارية", bg=CARD, fg=DARK, font=FT).pack(pady=(12, 4))
        r1 = tk.Frame(card1, bg=CARD); r1.pack(fill="x", padx=20, pady=4)
        tk.Label(r1, text="طابعات ويندوز المثبتة:", bg=CARD, fg=DARK, font=FB).pack(side="right", padx=(0, 8))
        self.cb_printer = ttk.Combobox(r1, font=F, width=32, state="readonly")
        self.cb_printer.pack(side="right", padx=6)
        self.cb_printer.bind("<<ComboboxSelected>>", lambda e: self.on_printer_selected())
        b_ref = self.mk_btn(r1, "🔄 تحديث القائمة", self.refresh_printer_list, "#475569")
        b_ref.pack(side="right", padx=6)
        add_tip(b_ref, "إعادة جلب قائمة الطابعات المثبتة من ويندوز")
        r2 = tk.Frame(card1, bg=CARD); r2.pack(fill="x", padx=20, pady=(2, 4))
        b_test = self.mk_btn(r2, "🖨 طباعة تجريبية", self.test_print, "#0d9488")
        b_test.pack(side="right", padx=6)
        add_tip(b_test, "طباعة صفحة اختبار قصيرة للتأكد أن الطابعة والتشكيل العربي يعملان")
        self.lbl_print_status = tk.Label(r2, text="", bg=CARD, fg=GRAY,
                                         font=("Segoe UI", 10, "bold"))
        self.lbl_print_status.pack(side="right", padx=8)

        # بطاقة بيانات التقرير المطبوع: اسم المحل + الطباعة التلقائية عند الإغلاق
        card2 = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card2.pack(fill="x", padx=25, pady=8)
        tk.Label(card2, text="🏪 بيانات التقرير المطبوع", bg=CARD, fg=DARK, font=FT).pack(pady=(12, 4))
        r3 = tk.Frame(card2, bg=CARD); r3.pack(fill="x", padx=20, pady=4)
        tk.Label(r3, text="اسم المحل:", bg=CARD, fg=DARK, font=FB).pack(side="right", padx=(0, 8))
        self.e_store = tk.Entry(r3, font=F, justify="center", relief="solid", bd=1, width=34)
        self.e_store.pack(side="right", padx=6, ipady=4)
        r4 = tk.Frame(card2, bg=CARD); r4.pack(fill="x", padx=20, pady=(2, 4))
        self.var_auto_print = tk.BooleanVar(value=False)
        cb_auto = tk.Checkbutton(r4, text="🖨 طباعة تقرير اليوم تلقائياً عند الإغلاق",
                                 variable=self.var_auto_print, font=FB, bg=CARD, fg=DARK,
                                 selectcolor="#dbeafe", activebackground=CARD, cursor="hand2")
        cb_auto.pack(side="right", padx=6)
        add_tip(cb_auto, "عند تفعيلها يُطبع تقرير اليوم مباشرة بعد حفظ إغلاقه دون سؤال")
        r5 = tk.Frame(card2, bg=CARD); r5.pack(fill="x", padx=20, pady=(2, 12))
        b_save = self.mk_btn(r5, "💾 حفظ الإعدادات", self.save_print_settings, ACCENT)
        b_save.pack(side="right", padx=6)
        add_tip(b_save, "حفظ اسم المحل وخيار الطباعة التلقائية في الإعدادات")

        # ★ إضافة (إصدار 9 — الميزة 8): بطاقة خلفية شاشة الدخول (اختيارية
        # للمدير) — زر اختيار صورة png/jpg للمحل تُحوّل تلقائياً عبر pillow
        # وتُحفظ باسم ثابت في مجلد البيانات ومسارها في settings، وتُعرض خلف
        # بطاقة الدخول بطبقة داكنة شفافة فوقها، مع زر إزالة يعيد الخلفية
        # المتدرجة الافتراضية — وتسجيل التعيين/الإزالة في سجل التدقيق
        card3 = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        card3.pack(fill="x", padx=25, pady=8)
        tk.Label(card3, text="🖼️ خلفية شاشة الدخول (اختيارية)", bg=CARD, fg=DARK, font=FT).pack(pady=(12, 4))
        r6 = tk.Frame(card3, bg=CARD); r6.pack(fill="x", padx=20, pady=4)
        self.lbl_login_bg_state = tk.Label(r6, text="", bg=CARD, fg=GRAY,
                                           font=("Segoe UI", 10, "bold"))
        self.lbl_login_bg_state.pack(side="right", padx=8)
        b_pick = self.mk_btn(r6, "🖼 اختيار صورة الخلفية", self.choose_login_bg_image, ACCENT)
        b_pick.pack(side="right", padx=6)
        add_tip(b_pick, "اختر صورة png/jpg للمحل — تُحوّل تلقائياً وتظهر خلف شاشة الدخول بطبقة داكنة تحفظ وضوح الحقول")
        b_rm = self.mk_btn(r6, "🗑 إزالة الصورة", self.remove_login_bg_image, "#64748b")
        b_rm.pack(side="right", padx=6)
        add_tip(b_rm, "حذف صورة الخلفية والعودة إلى التدرج الكحلي الافتراضي")
        self.lbl_login_bg_preview = tk.Label(card3, bg=CARD)
        self.lbl_login_bg_preview.pack(pady=(2, 12))
        self.refresh_login_bg_controls()

        # تحميل القيم المحفوظة الحالية من جدول settings
        try:
            self.e_store.insert(0, get_setting("store_name") or "")
            self.var_auto_print.set(get_setting("auto_print_daily") == "1")
        except Exception:
            pass
        self.refresh_printer_list()

        # ملاحظة أمر التثبيت — تظهر فقط إن لم تكن مكتبات الطباعة مثبتة
        if not PRINT_LIBS_OK:
            tk.Label(p, text="يتطلب: pip install pillow arabic-reshaper python-bidi",
                     bg=BG, fg=RED, font=("Segoe UI", 10, "bold")).pack(pady=(2, 14))
        # ★ إضافة (إصدار 7 — الميزة 9): سطر توضيحي جديد فقط — تقارير A4
        # تُطبع عبر نافذة «معاينة قبل الطباعة» وملفات PDF ولا تحتاج اختيار
        # طابعة مسبقاً (تُختار طابعة A4 من حوار الطباعة في ويندوز نفسه)
        tk.Label(p, text="📄 تقارير A4 تُطبع عبر نافذة «معاينة قبل الطباعة» وملفات PDF قياسية — "
                         "تختار طابعة A4 من حوار الطباعة في ويندوز نفسه ولا تحتاج تحديدها هنا مسبقاً.",
                 bg=BG, fg=GRAY, font=("Segoe UI", 10, "bold"), wraplength=840,
                 justify="right").pack(pady=(2, 8))
        # ★ ملاحظة أمر تثبيت reportlab — تظهر فقط إن لم تكن المكتبة مثبتة
        # (نفس أسلوب معالجة مكتبات الطباعة الحرارية الحالية تماماً)
        if not PDF_LIBS_OK:
            tk.Label(p, text="لتقارير A4: pip install reportlab",
                     bg=BG, fg=RED, font=("Segoe UI", 10, "bold")).pack(pady=(2, 14))

    def refresh_printer_list(self):
        """★ إضافة (إصدار 6): جلب قائمة الطابعات من ويندوز وعرضها في القائمة
        المنسدلة — والطابعة المحفوظة في الإعدادات تُحدد تلقائياً إن وُجدت"""
        try:
            printers = get_windows_printers()
            self.cb_printer["values"] = printers
            cur = self.cb_printer.get().strip()
            saved = get_setting("printer_name") or ""
            pick = cur if cur in printers else (saved if saved in printers else "")
            self.cb_printer.set(pick)
            if printers:
                self.lbl_print_status.config(
                    text=f"✔ تم العثور على {len(printers)} طابعة مثبتة", fg=GREEN)
            else:
                self.lbl_print_status.config(
                    text="لم يتم العثور على طابعات مثبتة على هذا الجهاز", fg=RED)
        except Exception as e:
            log_error(e)
            self.lbl_print_status.config(text="تعذر جلب قائمة الطابعات", fg=RED)

    def on_printer_selected(self):
        """★ إضافة (إصدار 6): اختيار الطابعة يُحفظ فوراً في جدول settings
        الموجود (المفتاح printer_name) — كما تنص المواصفة تماماً"""
        try:
            name = self.cb_printer.get().strip()
            if name:
                set_setting("printer_name", name)
                self.lbl_print_status.config(text=f"✔ تم اختيار الطابعة: {name}", fg=GREEN)
        except Exception as e:
            log_error(e)

    def test_print(self):
        """★ إضافة (إصدار 6): طباعة صفحة اختبار قصيرة (اسم النظام + سطر تجريبي
        عربي + التاريخ + الوقت) للتأكد أن كل شيء يعمل قبل الاعتماد على الطباعة"""
        try:
            name = self.cb_printer.get().strip() or (get_setting("printer_name") or "")
            if not name:
                messagebox.showwarning("تنبيه", "اختر الطابعة أولاً من القائمة")
                return
            set_setting("printer_name", name)   # حفظ المختار إن كان جديداً
            if print_report_lines(name, build_test_page_lines(), job_title="طباعة تجريبية"):
                audit("طباعة تجريبية", name)   # ★ تسجيل الطباعة التجريبية في سجل التدقيق
                messagebox.showinfo("تم", "أُرسلت صفحة الاختبار إلى الطابعة ✅")
        except Exception as e:
            log_error(e, sys.exc_info()[2])

    def save_print_settings(self):
        """★ إضافة (إصدار 6): حفظ اسم المحل وخيار الطباعة التلقائية والطابعة
        المختارة في جدول settings الموجود — مع تسجيل الحفظ في سجل التدقيق"""
        try:
            name = self.cb_printer.get().strip()
            if name:
                set_setting("printer_name", name)
            set_setting("store_name", self.e_store.get().strip())
            set_setting("auto_print_daily", "1" if self.var_auto_print.get() else "0")
            audit("حفظ إعدادات الطباعة",
                  f"الطابعة: {name or 'غير محددة'} — الطباعة التلقائية: "
                  + ("مفعلة" if self.var_auto_print.get() else "معطلة"))
            self.lbl_print_status.config(text="✔ تم حفظ إعدادات الطباعة", fg=GREEN)
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ", "تعذر حفظ إعدادات الطباعة")

    # ---------- ★ إضافات الإصدار 9 (الميزة 8): خلفية شاشة الدخول ----------
    def choose_login_bg_image(self):
        """★ إضافة (إصدار 9 — الميزة 8): اختيار صورة خلفية شاشة الدخول —
        filedialog تقبل png/jpg وتُحوّل png عبر pillow (المثبتة أصلاً) وتُحفظ
        باسم ثابت في مجلد البيانات، ومسارها في settings (المفتاح login_bg)
        مع تسجيل التعيين في سجل التدقيق"""
        if not LOGIN_BG_PIL_OK:
            messagebox.showwarning("تحتاج pillow", "اختيار صورة الخلفية يحتاج مكتبة pillow:\n"
                                    "pip install pillow")
            return
        p = filedialog.askopenfilename(title="اختيار صورة خلفية شاشة الدخول", parent=self,
                                       filetypes=[("صور", "*.png *.jpg *.jpeg *.bmp"),
                                                  ("كل الملفات", "*.*")])
        if not p:
            return
        try:
            img = _BGImage.open(p).convert("RGB")
            img.save(login_bg_file(), "PNG")       # تحويل موحّد إلى png باسم ثابت
            set_setting("login_bg", login_bg_file())
            audit("تعيين صورة خلفية الدخول", os.path.basename(p))
            self.refresh_login_bg_controls()
            messagebox.showinfo("تم", "تم تعيين صورة الخلفية — ستظهر خلف شاشة الدخول القادمة")
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ", f"تعذر تحميل الصورة:\n{e}")

    def remove_login_bg_image(self):
        """★ إضافة (إصدار 9 — الميزة 8): إزالة الصورة والعودة للخلفية المتدرجة
        الافتراضية — مع تسجيل الإزالة في سجل التدقيق"""
        try:
            set_setting("login_bg", "")
            try:
                if os.path.exists(login_bg_file()):
                    os.remove(login_bg_file())
            except Exception:
                pass
            audit("إزالة صورة خلفية الدخول")
            self.refresh_login_bg_controls()
            messagebox.showinfo("تم", "أُزيلت الصورة — عادت الخلفية المتدرجة الافتراضية")
        except Exception as e:
            log_error(e)
            messagebox.showerror("خطأ", "تعذرت الإزالة")

    def refresh_login_bg_controls(self):
        """★ إضافة (إصدار 9 — الميزة 8): تحديث حالة ومعاينة مصغرة لخلفية الدخول
        في شاشة إعدادات الطباعة — وأي فشل يُعرض بهدوء دون رسائل مزعجة"""
        try:
            if not hasattr(self, "lbl_login_bg_state"):
                return
            path = get_setting("login_bg")
            on = bool(path) and os.path.exists(path) and LOGIN_BG_PIL_OK
            self.lbl_login_bg_state.config(
                text=("✔ معيّنة — ستظهر خلف شاشة الدخول" if on
                      else "غير معيّنة — الخلفية المتدرجة الافتراضية"),
                fg=(GREEN if on else GRAY))
            self.lbl_login_bg_preview.config(image="", text="")
            self.lbl_login_bg_preview.image = None
            if on:
                try:
                    img = _BGImage.open(path)
                    img.thumbnail((240, 130))
                    ph = _BGImageTk.PhotoImage(img)
                    self.lbl_login_bg_preview.config(image=ph)
                    self.lbl_login_bg_preview.image = ph   # مرجع حي يمنع محو الصورة
                except Exception:
                    self.lbl_login_bg_preview.config(text="(تعذر عرض المعاينة)")
        except Exception as e:
            log_error(e)

    # ---------- (6) إعادة طباعة أي يوم من الأرشيف ----------
    def print_selected_day(self):
        """★ إضافة (إصدار 6): طباعة تقرير اليوم المحدد من شريط الأرشيف"""
        sel = self.tv_arch.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر يوماً من الجدول أولاً"); return
        self.print_day_report(sel[0], reprint=True)

    def print_day_report(self, d, reprint=False, closer=None, when=""):
        """★ إضافة (إصدار 6): طباعة تقرير إغلاق يوم من بيانات daily_reports
        المحفوظة (نقداً/شبكة/مرتجعات/الإجمالي/عدد العمليات/وقت الإغلاق) — عند
        الإعادة يظهر سطر «إعادة طباعة» بالوقت الحالي، وكل طباعة ناجحة تُسجل
        في سجل التدقيق باسم من طبع. أي فشل يعرض رسالة عربية ويسجل في
        error_log ولا يوقف البرنامج أبداً"""
        try:
            with connect() as conn:
                rep = conn.execute("SELECT * FROM daily_reports WHERE report_date=?",
                                   (d,)).fetchone()
            if rep is None:
                messagebox.showinfo("تنبيه", f"لا يوجد تقرير محفوظ ليوم {d}")
                return
            # من أغلق اليوم: من سجل التدقيق إن لم يُمرر مباشرة (إعادة الطباعة)
            who = closer or get_day_closer(d) or CURRENT_USER["name"]
            lines = build_day_report_lines(
                store_name=get_setting("store_name") or "",
                d=d, ops_count=rep["ops_count"] or 0,
                cash=rep["total_cash"] or 0, netw=rep["total_network"] or 0,
                rets=rep["total_returns"] or 0, net=rep["net_total"] or 0,
                closed_at=rep["closed_at"], closed_by=who, reprint=reprint)
            if print_report_lines(get_setting("printer_name") or "", lines,
                                  job_title=f"تقرير يوم {d}"):
                audit("طباعة تقرير يوم",
                      d + (" — إعادة طباعة" if reprint else (" — " + when if when else "")))
        except Exception as e:
            log_error(e, sys.exc_info()[2])

    # ═══════════════════════════════════════════════════════════
    # ★★★ إضافات الإصدار 7 — شاشة النسخ والاستعادة + المعاينة قبل الطباعة ★★★
    # ═══════════════════════════════════════════════════════════

    # ---------- (الطبقة 4) شاشة النسخ والاستعادة — للمدير فقط ----------
    def show_backups(self):
        """★ إضافة (إصدار 7): فتح شاشة النسخ والاستعادة — للمدير فقط"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): صلاحية «النسخ والاستعادة» بدل «المدير فقط»
        if not self.require_admin("backup"):
            return
        self.show_page("backups")
        self.refresh_backups_list()

    def build_backups_page(self, p):
        """★ إضافة (إصدار 7 — الطبقة 4): شاشة «🗄️ النسخ والاستعادة» — جدول
        بكل النسخ (النوع/الاسم/التاريخ/المكان/الحجم بالكيلوبايت/عدد العمليات
        داخل النسخة) + نسخة فورية الآن + استعادة نسخة مختارة + اختيار مجلد
        النسخ الخارجي + فتح مجلد النسخ + تصدير كل البيانات (طوارئ)"""
        self.page_head(p, "🗄️ النسخ والاستعادة",
                       "حماية البيانات — نسخ يومية وشهرية وفورية واستعادة آمنة — للمدير فقط")

        # بطاقة معلومات مجلدات النسخ: الداخلي والخارجي
        info = tk.Frame(p, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        info.pack(fill="x", padx=25, pady=6)
        tk.Label(info, text="مجلد النسخ الداخلي (بجانب البرنامج):", bg=CARD, fg=DARK,
                 font=FB).pack(pady=(12, 2))
        tk.Label(info, text=BACKUP_ROOT, bg=CARD, fg=GRAY, font=("Consolas", 9)).pack(pady=(0, 6))
        self.lbl_bk_external = tk.Label(info, text="", bg=CARD, fg=GRAY,
                                        font=("Segoe UI", 10, "bold"), wraplength=860)
        self.lbl_bk_external.pack(pady=(0, 12))

        # صف الأزرار: نسخة فورية / استعادة / مجلد خارجي / فتح المجلد / تصدير طوارئ / تحديث
        bar = tk.Frame(p, bg=BG); bar.pack(fill="x", padx=25, pady=6)
        b_now = self.mk_btn(bar, "📋 نسخة فورية الآن", self.make_instant_now, GREEN)
        b_now.pack(side="right", padx=5)
        add_tip(b_now, "نسخة يدوية فورية من قاعدة البيانات باسم instant_التاريخ_الوقت (يُحتفظ بآخر 10)")
        b_rest = self.mk_btn(bar, "♻️ استعادة نسخة مختارة", self.restore_selected_backup, ORANGE)
        b_rest.pack(side="right", padx=5)
        add_tip(b_rest, "استبدال القاعدة الحالية بنسخة مختارة — بعد فحص صحتها وأخذ نسخة أمان تلقائياً")
        b_ext = self.mk_btn(bar, "📂 اختيار مجلد النسخ الخارجي", self.choose_external_dir, "#0369a1")
        b_ext.pack(side="right", padx=5)
        add_tip(b_ext, "اختيار مجلد خارجي (فلاش/قرص آخر) تُنسخ إليه النسخ اليومية والشهرية إضافة للداخلي")
        b_open = self.mk_btn(bar, "🖥 فتح مجلد النسخ", self.open_backups_folder, "#475569")
        b_open.pack(side="right", padx=5)
        add_tip(b_open, "فتح مجلد النسخ الاحتياطي في مستكشف ويندوز")
        b_emg = self.mk_btn(bar, "📤 تصدير كل البيانات (طوارئ)", self.export_emergency, RED)
        b_emg.pack(side="right", padx=5)
        add_tip(b_emg, "ملف Excel شامل بكل البيانات (العمليات/التقارير/المستخدمون/سجل التدقيق)")
        b_ref = self.mk_btn(bar, "🔄 تحديث", self.refresh_backups_list, "#475569")
        b_ref.pack(side="right", padx=5)
        add_tip(b_ref, "إعادة تحميل جدول النسخ من مجلدات النسخ الداخلية والخارجية")

        # جدول النسخ: النوع | اسم النسخة | التاريخ | المكان | الحجم | عدد العمليات
        frm, self.tv_backups = self.mk_tree(p,
            ["عدد العمليات", "الحجم (KB)", "المكان", "التاريخ", "اسم النسخة", "النوع"],
            [100, 100, 90, 105, 250, 115])
        frm.pack(fill="both", expand=True, padx=25, pady=8)
        self.tv_backups.tag_configure("monthly", background="#dcfce7")   # شهرية: خلفية خضراء فاتحة
        self.tv_backups.tag_configure("instant", background="#e0f2fe")   # فورية: خلفية زرقاء فاتحة
        self.tv_backups.tag_configure("safety", background="#fef3c7")    # أمان استعادة: برتقالية فاتحة

        # سياسة الاحتفاظ — سطر توضيحي أسفل الشاشة
        self.lbl_bk_policy = tk.Label(p, text="", bg=BG, fg=GRAY,
                                      font=("Segoe UI", 10, "bold"), wraplength=900, justify="right")
        self.lbl_bk_policy.pack(fill="x", padx=25, pady=(0, 16))
        self.backups_list = []     # بيانات الجدول الحالية (تُستخدم عند الاستعادة)

    def refresh_backups_list(self):
        """★ إضافة (إصدار 7 — الطبقة 4): تحميل كل النسخ في الجدول — الداخلية
        والخارجية معاً، مع عدد العمليات داخل كل نسخة وبتحديث حالة المجلد الخارجي"""
        # ★ تعديل مصرح به (إصدار 8 — الميزة 5): فحص الصلاحية الدقيقة بدل «المدير فقط»
        if not self.has_permission("backup"):
            return
        self.backups_list = list_all_backups()
        self.tv_backups.delete(*self.tv_backups.get_children())
        for i, b in enumerate(self.backups_list):
            tag = ("monthly" if b["type"] == "شهرية" else
                   "instant" if b["type"] == "فورية" else
                   "safety" if b["type"] == "أمان استعادة" else "")
            self.tv_backups.insert("", "end", iid=str(i), tags=(tag,) if tag else (),
                values=((str(b["ops"]) if b["ops"] >= 0 else "—"), b["size"], b["place"],
                        b["date"], b["name"], b["type"]))
        ext = get_setting("external_backup_dir")
        self.lbl_bk_external.config(
            text=("مجلد النسخ الخارجي: " + ext if ext
                  else "⚠ لم يتم اختيار مجلد نسخ خارجي بعد — يُنصح باختيار فلاش/قرص خارجي للنسخ في مكانين"),
            fg=(GRAY if ext else ORANGE))
        n_daily = sum(1 for b in self.backups_list if b["type"] == "يومية")
        n_month = sum(1 for b in self.backups_list if b["type"] == "شهرية")
        n_inst = sum(1 for b in self.backups_list if b["type"] == "فورية")
        self.lbl_bk_policy.config(
            text=(f"النسخ: {n_daily} يومية (آخر 30 تلقائياً) — {n_month} شهرية (دائمة لا تُحذف) — "
                  f"{n_inst} فورية (آخر 10) — تُنشأ نسخة يومية تلقائياً عند كل إغلاق يوم ناجح "
                  "وفشل النسخ لا يلغي الإغلاق أبداً"))

    def make_instant_now(self):
        """★ إضافة (إصدار 7 — الطبقة 4): زر «📋 نسخة فورية الآن» — نسخة يدوية
        فورية تُسجل في سجل التدقيق ويُحدَّث الجدول بعدها مباشرة"""
        try:
            path = make_instant_backup()
            self.refresh_backups_list()
            messagebox.showinfo("تم", "تم إنشاء النسخة الفورية بنجاح ✅\n"
                                        + os.path.basename(path))
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ", f"تعذر إنشاء النسخة الفورية:\n{e}")

    def choose_external_dir(self):
        """★ إضافة (إصدار 7 — الطبقة 3): زر «اختيار مجلد النسخ الخارجي» —
        filedialog يختار مجلداً خارجياً يُحفظ مكانه في settings
        (external_backup_dir) وتُنسخ إليه كل نسخة يومية وشهرية قادمة إضافة
        للمجلد الداخلي، وكل تغيير يُسجل في سجل التدقيق"""
        d = filedialog.askdirectory(title="اختيار مجلد النسخ الخارجي (فلاش / قرص خارجي)")
        if not d:
            return
        set_setting("external_backup_dir", d)
        audit("تغيير مجلد النسخ الخارجي", d)
        self.refresh_backups_list()
        messagebox.showinfo("تم",
            "تم تعيين مجلد النسخ الخارجي ✅\n" + d +
            "\n\nكل نسخة يومية وشهرية قادمة ستُنسخ في المكانين معاً (داخلي + خارجي)،"
            "\nوإن فشل الخارجي تستمر النسخة الداخلية مع رسالة تحذير.")

    def open_backups_folder(self):
        """★ إضافة (إصدار 7 — الطبقة 3): زر «فتح مجلد النسخ» — يفتح مجلد
        backups في مستكشف ملفات ويندوز"""
        try:
            ensure_backup_dirs()
            if os.name == "nt":
                os.startfile(BACKUP_ROOT)
            else:
                messagebox.showinfo("مجلد النسخ", BACKUP_ROOT)
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ", f"تعذر فتح مجلد النسخ:\n{e}")

    def restore_selected_backup(self):
        """★ إضافة (إصدار 7 — الطبقة 4): زر «♻️ استعادة نسخة مختارة» — فحص
        صحة النسخة أولاً (فتحها بـ sqlite3 وقراءة جدول) ثم تحذير قوي بالعربية
        يوضح أن الاستعادة تستبدل القاعدة الحالية، ثم نسخة أمان تلقائية من
        الوضع الحالي (pre_restore_...) ثم الاستبدال الذري ثم رسالة إعادة
        تشغيل البرنامج — والنسخة التالفة تُرفض برسالة واضحة"""
        sel = self.tv_backups.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر نسخة من الجدول أولاً"); return
        rec = self.backups_list[int(sel[0])]
        path = rec["path"]
        # 1) فحص صحة ملف النسخة قبل أي شيء
        ok, msg = check_backup_health(path)
        if not ok:
            messagebox.showerror("نسخة تالفة — رُفضت الاستعادة",
                "فشل فحص صحة هذه النسخة ولن تُستخدم:\n\n" + msg)
            return
        # 2) تحذير قوي بالعربية (تأكيد مزدوج)
        warn = ("⚠️ تحذير هام ⚠️\n\n"
                "الاستعادة ستستبدل قاعدة البيانات الحالية بالكامل ببيانات النسخة:\n"
                f"{rec['name']}  ({rec['type']} — {rec['date']})\n"
                f"النتيجة: {msg}\n\n"
                "كل العمليات التي تمت بعد هذه النسخة ستُفقد.\n"
                "سيُنشئ البرنامج تلقائياً نسخة أمان من الوضع الحالي قبل الاستعادة.\n\n"
                "هل أنت متأكد من المتابعة؟")
        if not messagebox.askyesno("تأكيد الاستعادة (1 من 2)", warn):
            return
        if not messagebox.askyesno("تأكيد الاستعادة (2 من 2)",
                "تأكيد أخير:\nهل تريد فعلاً استبدال القاعدة الحالية بهذه النسخة الآن؟"):
            return
        # 3) نسخة الأمان ثم الاستبدال الذري ثم رسالة إعادة التشغيل
        try:
            safety_name = restore_backup_file(path)
            audit("استعادة نسخة", f"{rec['name']} — نسخة الأمان: {safety_name}")
            messagebox.showinfo("تمت الاستعادة ✅",
                "استُبدلت قاعدة البيانات ببيانات النسخة بنجاح.\n"
                "نُشئت نسخة أمان من الوضع السابق باسم:\n" + safety_name +
                "\n\n⚠ أغلق البرنامج الآن وافتحه من جديد لتفعيل البيانات المستعادة.")
            self.exit_app()          # إغلاق البرنامج — يجب إعادة تشغيله بعد الاستعادة
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("فشلت الاستعادة",
                "تعذر استعادة النسخة:\n" + str(e) +
                "\n\nلم تتغير قاعدة البيانات الحالية (راجع error_log.txt).")

    def export_emergency(self):
        """★ إضافة (إصدار 7 — الطبقة 5): زر «📤 تصدير كل البيانات (طوارئ)» —
        ملف xlsx متعدد الأوراق (العمليات/التقارير اليومية/المستخدمون/سجل
        التدقيق) عبر export_xlsx_multi الجديدة بنفس منطق zip الموجود"""
        path = filedialog.asksaveasfilename(title="تصدير كل البيانات (طوارئ)",
                                            defaultextension=".xlsx",
                                            initialfile=f"تصدير_شامل_طوارئ_{today_str()}.xlsx",
                                            filetypes=[("ملف Excel", "*.xlsx")])
        if not path:
            return
        try:
            with connect() as conn:
                ops = conn.execute("SELECT date, item_name, customer_name, seller_name,"
                                   " quantity, price, total, type FROM operations"
                                   " ORDER BY date, id").fetchall()
                reps = conn.execute("SELECT report_date, ops_count, total_cash, total_network,"
                                    " total_sales, total_returns, net_total, closed_at"
                                    " FROM daily_reports ORDER BY report_date").fetchall()
                usrs = conn.execute("SELECT username, role,"
                                    " CASE WHEN active=1 THEN 'مفعل' ELSE 'موقوف' END, created_at"
                                    " FROM users ORDER BY id").fetchall()
                aud = conn.execute("SELECT ts, username, action, details FROM audit_log"
                                   " ORDER BY id").fetchall()
            export_xlsx_multi(path, [
                ("العمليات",
                 ["التاريخ", "اسم الصنف", "العميل", "البائع", "الكمية", "السعر", "المبيع", "النوع"],
                 [tuple(r) for r in ops],
                 [12, 26, 20, 16, 10, 10, 12, 10]),
                ("التقارير اليومية",
                 ["التاريخ", "عدد العمليات", "نقداً", "شبكة", "المبيعات", "المرتجعات", "الإجمالي", "وقت الإغلاق"],
                 [tuple(r) for r in reps],
                 [12, 12, 14, 14, 14, 14, 14, 18]),
                ("المستخدمون",
                 ["اسم المستخدم", "الدور", "الحالة", "تاريخ الإضافة"],
                 [tuple(r) for r in usrs],       # ★ بلا كلمات المرور أبداً — أمان
                 [20, 12, 12, 18]),
                ("سجل التدقيق",
                 ["التاريخ والوقت", "المستخدم", "الإجراء", "التفاصيل"],
                 [tuple(r) for r in aud],
                 [18, 16, 20, 40]),
            ], desc="تصدير طوارئ شامل — كل البيانات")
            messagebox.showinfo("تم", "تم تصدير كل البيانات بنجاح ✅\n" + path)
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ", f"تعذر التصدير:\n{e}")

    # ---------- (الميزة 7+8) المعاينة قبل الطباعة ومسار A4 ----------
    def print_selected_day_a4(self):
        """★ إضافة (إصدار 7 — الميزة 8): زر «🖨 طباعة/معاينة A4» في شريط
        الأرشيف — يفتح نافذة المعاينة لتقرير اليوم المحدد قبل أي طباعة"""
        sel = self.tv_arch.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر يوماً من الجدول أولاً"); return
        self.open_print_preview("day", sel[0])

    def print_period_report(self):
        """★ إضافة (إصدار 7 — الميزة 8): زر «📄 تقرير الفترة A4» — تقرير دوري
        لكل الأيام ضمن مدى التاريخ المُصفّى في الأرشيف، بعنوان «تقرير فترة من
        [تاريخ] إلى [تاريخ]» مع جدول الأيام والإجمالي التراكمي — عبر المعاينة"""
        f, t = parse_date_multi(self.e_from.get()), parse_date_multi(self.e_to.get())
        bad = [lbl for lbl, v in (("من تاريخ", f), ("إلى تاريخ", t)) if v is None]
        if bad:
            messagebox.showwarning("تاريخ خاطئ",
                "صيغة غير صحيحة لـ " + " و ".join(bad) +
                "\nالصيغ المقبولة: 2025-01-10 أو 10-01-2025 أو 10/01/2025")
            return
        if not f and not t:
            messagebox.showinfo("تنبيه",
                "أدخل مدى التاريخ أولاً في حقلي «من تاريخ» و«إلى تاريخ» بالأعلى ثم اضغط «🔍 تصفية»")
            return
        sql, params, cond = "SELECT * FROM daily_reports", [], []
        if f:
            cond.append("report_date >= ?"); params.append(f)
        if t:
            cond.append("report_date <= ?"); params.append(t)
        if cond:
            sql += " WHERE " + " AND ".join(cond)
        sql += " ORDER BY report_date"
        with connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        if not rows:
            messagebox.showinfo("تنبيه", "لا توجد أيام مغلقة ضمن هذا المدى"); return
        dates = [r["report_date"] for r in rows]
        self.open_print_preview("period", (f or min(dates), t or max(dates), rows))

    def open_print_preview(self, kind, arg):
        """★ إضافة (إصدار 7 — الميزة 7): نافذة «👁️ معاينة قبل الطباعة» الكبيرة
        (900×700) — تعرض المحتوى المراد طباعته كما سيُطبع تماماً (الترويسة
        والتواريخ والصفوف والإجماليات) وأسفلها ثلاثة أزرار: «طباعة A4 (PDF)»
        تفتح حوار الطباعة القياسي في ويندوز (تختار طابعة A4 منه فتختفي مشكلة
        الصفحات البيضاء نهائياً) و«طباعة حرارية 80mm» على الطابعة المختارة في
        الإعدادات بنفس نظام ESC/POS الموجود و«إلغاء» — المعاينة مطلوبة دائماً
        قبل أي طباعة A4 ولا طباعة مباشرة بدونها"""
        store = get_setting("store_name") or "نظام المبيعات والمُرتجعات"
        if kind == "day":
            d = arg
            with connect() as conn:
                rep = conn.execute("SELECT * FROM daily_reports WHERE report_date=?",
                                   (d,)).fetchone()
            if rep is None:
                messagebox.showinfo("تنبيه", f"لا يوجد تقرير محفوظ ليوم {d}")
                return
            title = f"تقرير إغلاق اليوم — {day_name(d)} {d}"
            sub = f"وقت الإغلاق: {rep['closed_at'] or '—'}"
            data = {"d": d, "rep": rep}
        else:
            f, t, rows = arg
            title = f"تقرير فترة من {f} إلى {t}"
            sub = f"عدد الأيام: {len(rows)}"
            data = {"f": f, "t": t, "rows": rows}
        # ★ إضافة (إصدار 8 — الميزة 3): تسجيل نافذة المعاينة في التتبع المركزي
        win = self.register_window(tk.Toplevel(self))
        win.title("👁️ معاينة قبل الطباعة")
        win.geometry("900x700"); win.configure(bg=BG)

        # ترويسة المعاينة — كما ستُطبع تماماً: اسم المحل والعنوان والتاريخ
        head = tk.Frame(win, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        head.pack(fill="x", padx=22, pady=(16, 6))
        tk.Label(head, text=store, bg=CARD, fg=DARK, font=FT).pack(pady=(12, 2))
        tk.Label(head, text=title, bg=CARD, fg=ACCENT,
                 font=("Segoe UI", 13, "bold")).pack(pady=2)
        tk.Label(head, text=sub, bg=CARD, fg=GRAY,
                 font=("Segoe UI", 10)).pack(pady=(0, 12))

        # محتوى المعاينة — نفس الصفوف والإجماليات التي ستُطبع
        body = tk.Frame(win, bg=BG)
        body.pack(fill="both", expand=True, padx=22, pady=4)
        if kind == "day":
            rep = data["rep"]
            closer = get_day_closer(d) or CURRENT_USER["name"]
            frm, tv = self.mk_tree(body, ["القيمة", "البند"], [300, 280])
            frm.pack(fill="both", expand=True, pady=(0, 4))
            tv.tag_configure("total", background="#dbeafe")
            rows = [("عدد العمليات", str(rep["ops_count"] or 0)),
                    ("مبيعات نقداً", money(rep["total_cash"] or 0)),
                    ("مبيعات شبكة", money(rep["total_network"] or 0)),
                    ("المرتجعات", money(rep["total_returns"] or 0)),
                    ("إجمالي اليوم", money(rep["net_total"] or 0)),
                    ("أغلق بواسطة", closer)]
            for i, (k, v) in enumerate(rows):
                tv.insert("", "end", tags=("total",) if k == "إجمالي اليوم" else (),
                          iid=str(i), values=(v, k))
            tk.Label(body, text="شكراً لزيارتكم", bg=BG, fg=GRAY,
                     font=("Segoe UI", 10, "bold")).pack(pady=(0, 4))
        else:
            rows = data["rows"]
            frm, tv = self.mk_tree(body,
                ["الإجمالي", "المرتجعات", "شبكة", "نقداً", "عدد العمليات", "التاريخ"],
                [110, 105, 100, 100, 95, 105])
            frm.pack(fill="both", expand=True, pady=(0, 4))
            tv.tag_configure("total", background="#dbeafe")
            t_cash = t_netw = t_rets = t_net = 0.0; t_ops = 0
            for r in rows:
                cash, netw = r["total_cash"] or 0, r["total_network"] or 0
                rets, net = r["total_returns"] or 0, r["net_total"] or 0
                t_cash += cash; t_netw += netw; t_rets += rets; t_net += net
                t_ops += r["ops_count"] or 0
                tv.insert("", "end", values=(money(net), money(rets), money(netw),
                                             money(cash), r["ops_count"], r["report_date"]))
            tv.insert("", "end", tags=("total",),
                      values=(money(t_net), money(t_rets), money(t_netw),
                              money(t_cash), t_ops, "الإجمالي التراكمي"))
            tk.Label(body, text=f"نقداً: {money(t_cash)} — شبكة: {money(t_netw)} — "
                                f"المرتجعات: {money(t_rets)} — عدد العمليات: {t_ops}",
                     bg=BG, fg=GRAY, font=("Segoe UI", 10, "bold")).pack(pady=(0, 4))

        # أزرار الطباعة الثلاثة أسفل المعاينة
        bar = tk.Frame(win, bg=BG)
        bar.pack(fill="x", padx=22, pady=(4, 16))
        b_a4 = self.mk_btn(bar, "🖨 طباعة A4 (PDF)",
                           lambda: self._preview_print_a4(kind, data), "#1d4ed8")
        b_a4.pack(side="right", padx=6)
        add_tip(b_a4, "يُنشأ ملف PDF قياسي ويُفتح حوار الطباعة في ويندوز — اختر طابعة A4 منه")
        b_th = self.mk_btn(bar, "🖨 طباعة حرارية 80mm",
                           lambda: self._preview_print_thermal(kind, data), "#334155")
        b_th.pack(side="right", padx=6)
        add_tip(b_th, "طباعة على الطابعة الحرارية المختارة في إعدادات الطباعة (نظام ESC/POS الموجود)")
        b_cancel = self.mk_btn(bar, "❌ إلغاء", win.destroy, "#475569")
        b_cancel.pack(side="right", padx=6)
        add_tip(b_cancel, "إغلاق نافذة المعاينة دون طباعة")

    def _preview_print_a4(self, kind, data):
        """★ إضافة (إصدار 7 — الميزة 6+7): تنفيذ طباعة A4 من المعاينة — ملف
        PDF قياسي يُحفظ مؤقتاً (مجلد pdf_reports بجانب البرنامج) ثم يُرسل
        للطباعة عبر حوار الطباعة القياسي، وكل طباعة تُسجل في سجل التدقيق
        بصيغة «طباعة A4 — [نوع التقرير]»"""
        # ★ إضافة (إصدار 8 — الميزة 5): صلاحية «تصدير التقارير (CSV/Excel/PDF)» —
        # طباعة A4 عبر ملف PDF هي أحد أنواع التصدير في النظام الدقيق
        if not self.has_permission("export_reports"):
            messagebox.showwarning("صلاحية", "ليست لديك صلاحية «تصدير التقارير»")
            return
        if not PDF_LIBS_OK:
            messagebox.showerror("طباعة A4 غير متاحة", PDF_LIBS_MSG)
            return
        try:
            store = get_setting("store_name") or ""
            folder = os.path.join(data_dir(), "pdf_reports")
            os.makedirs(folder, exist_ok=True)
            stamp = datetime.now().strftime("%H%M")
            if kind == "day":
                d, rep = data["d"], data["rep"]
                path = os.path.join(folder, f"تقرير_اليوم_{d}_{stamp}.pdf")
                build_day_report_pdf(path, store, d, rep["ops_count"] or 0,
                                     rep["total_cash"] or 0, rep["total_network"] or 0,
                                     rep["total_returns"] or 0, rep["net_total"] or 0,
                                     rep["closed_at"],
                                     get_day_closer(d) or CURRENT_USER["name"])
                label = f"تقرير إغلاق يوم {d}"
            else:
                f, t, rows = data["f"], data["t"], data["rows"]
                path = os.path.join(folder, f"تقرير_الفترة_{f}_{t}_{stamp}.pdf")
                build_period_report_pdf(path, store, f, t, rows)
                label = f"تقرير فترة من {f} إلى {t}"
            ok, err = send_pdf_to_printer(path)
            audit("طباعة A4 — " + label, os.path.basename(path))
            if ok:
                messagebox.showinfo("تم الإرسال للطباعة",
                    "أُرسل التقرير إلى حوار الطباعة ✅\n"
                    "اختر طابعة A4 من نافذة الطباعة التي ظهرت في ويندوز.\n\n"
                    "ملف PDF محفوظ في:\n" + path)
            else:
                messagebox.showwarning("افتح الملف واطبعه",
                    "تعذر فتح حوار الطباعة تلقائياً — فُتح ملف PDF بدلاً منه.\n"
                    "اطبع منه مباشرة (Ctrl+P) واختر طابعة A4.\n\n" + err + "\n\nالملف:\n" + path)
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ في طباعة A4",
                                 "حدث خطأ أثناء توليد ملف PDF:\n\n" + str(e))

    def _preview_print_thermal(self, kind, data):
        """★ إضافة (إصدار 7 — الميزة 7): زر «الطباعة الحرارية 80mm» من
        المعاينة — لنفس نظام ESC/POS الموجود: تقرير اليوم عبر الدالة الموجودة
        نفسها (print_day_report) وتقرير الفترة عبر أسطر حرارية جديدة"""
        try:
            if kind == "day":
                self.print_day_report(data["d"], reprint=True)
            else:
                f, t, rows = data["f"], data["t"], data["rows"]
                if print_report_lines(get_setting("printer_name") or "",
                                      build_period_report_lines(get_setting("store_name") or "",
                                                                f, t, rows),
                                      job_title=f"تقرير فترة {f} — {t}"):
                    audit("طباعة تقرير فترة", f"من {f} إلى {t} — {len(rows)} يوماً (حرارية)")
        except Exception as e:
            log_error(e, sys.exc_info()[2])

    # ═══════════════════════════════════════════════════════
    # ★★★ إضافة (إصدار 10 — نظام التحديث التلقائي الصامت) ★★★
    # شريط الإشعار الأصفر + نافذة التحديث للمدير — لا شيء تقني يظهر
    # للمستخدمين: البائع يرى الشريط و«راجع المدير» فقط
    # ═══════════════════════════════════════════════════════

    def refresh_update_bar(self):
        """(2) شريط الإشعار الأصفر الرفيع أعلى الشريط الإحصائي — الوحيد الذي
        يراه المستخدمون من نظام التحديث: بلا أي كلمة تقنية إطلاقاً — البائع
        يرى «راجع المدير» فقط، والمدير يرى زر «⬇️ تحديث الآن» وزر ✕ لإخفاء
        الشريط لهذه الجلسة فقط
        ★ إصلاح (11 — البندان ب+ج): (ب) زر «⬇️ التحديث» الجانبي يُدار من
        هنا أيضاً — مخفي بلا تحديث مؤكد وظهره الوحيد نتيجة مقارنة ناجحة
        (ج) نص الشريط يعرض رقم الإصدار الجديد: «🔔 يتوفر تحديث جديد —
        الإصدار [رقم]»، فإن غاب الرقم اكتمل النص بدونه"""
        # (ب) زر الشريط الجانبي أولاً: يظهر للمدير فقط عند تحديث مؤكد فعلياً —
        # وإلا يُخفى صراحة (هذه هي النقطة الوحيدة التي تُظهره بعد الإقلاع)
        b_side = self.nav_buttons.get("update")
        if b_side is not None:
            try:
                if (getattr(self, "update_available_version", None)
                        and self.role == "مدير" and self.has_permission("manager")):
                    try:
                        b_side.pack_info()      # محزوم أصلاً؟ لا تعد حزمه (يبقى موضعه)
                    except Exception:
                        b_side.pack(fill="x", padx=10, pady=3)
                else:
                    b_side.pack_forget()
            except Exception:
                pass
        if getattr(self, "update_bar", None) is not None:
            try:
                self.update_bar.destroy()
            except Exception:
                pass
            self.update_bar = None
        ver = getattr(self, "update_available_version", None)
        if not ver:
            return            # لا تحديث معروف
        # ★ إصلاح (1): الشريط الذي أُخفي بـ✕ لا يعود في نفس الجلسة إلا إذا
        # اكتشف الفحص رقماً أحدث فعلياً من رقم الشريط المخفي — رقم أحدث
        # واحد يعيده ويجدّد حالة الإخفاء للجلسة من جديد
        if getattr(self, "update_bar_dismissed", False):
            dver = getattr(self, "update_bar_dismissed_version", None)
            if dver and update_is_newer(ver, dver):
                self.update_bar_dismissed = False
                self.update_bar_dismissed_version = None
            else:
                return        # نفس الرقم المخفي أو أقدم منه — يبقى مخفياً
        upd_bg, upd_fg = "#fef9c3", "#854d0e"
        bar = tk.Frame(self.container, bg=upd_bg, highlightbackground="#fde047",
                       highlightthickness=1)
        try:                  # فوق الشريط الإحصائي مباشرة
            bar.pack(fill="x", padx=25, pady=(10, 0), before=self.stats_bar_frame)
        except Exception:
            bar.pack(fill="x", padx=25, pady=(10, 0))
        # (ج) النص مع رقم الإصدار الجديد — وبدونه إن غاب
        tk.Label(bar, text=(f"🔔 يتوفر تحديث جديد — الإصدار {ver}" if ver
                            else "🔔 يتوفر تحديث جديد"),
                 bg=upd_bg, fg=upd_fg,
                 font=("Segoe UI", 10, "bold")).pack(side="right", padx=(4, 12), pady=4)
        if self.role == "مدير":
            b_now = tk.Button(bar, text="⬇️ تحديث الآن", command=self.update_now_dialog,
                              bg=ORANGE, fg="white", activebackground=ORANGE,
                              activeforeground="white", font=("Segoe UI", 9, "bold"),
                              bd=0, cursor="hand2", padx=12, pady=2, highlightthickness=0)
            b_now.pack(side="left", padx=(12, 6), pady=3)
            add_tip(b_now, "تنزيل التحديث وتثبيته — يتطلب إعادة تشغيل البرنامج بعد التثبيت")
            # ★ إضافة (إصلاح 3 — البند أ): زر «فحص التحديثات الآن» داخل
            # الشريط الأصفر بجانب «تحديث الآن» — فحص فوري بنص الزر «جارٍ
            # الفحص...» أثناءه ثم رسالة نتيجة عربية دائماً
            b_chk = tk.Button(bar, text="🔄 فحص التحديثات الآن",
                              command=lambda: self.update_check_manual(b_chk),
                              bg="#0369a1", fg="white", activebackground="#0369a1",
                              activeforeground="white", font=("Segoe UI", 9, "bold"),
                              bd=0, cursor="hand2", padx=10, pady=2, highlightthickness=0)
            b_chk.pack(side="left", padx=(0, 6), pady=3)
            add_tip(b_chk, "فحص فوري جديد الآن برسالة نتيجة — يظهر الشريط فور توفر إصدار أحدث")
            b_x = tk.Button(bar, text="✕", command=self.dismiss_update_bar,
                            bg=upd_bg, fg=upd_fg, activebackground="#fde047",
                            activeforeground=upd_fg, font=("Segoe UI", 8, "bold"),
                            bd=0, relief="flat", cursor="hand2", padx=6, pady=1,
                            highlightthickness=0, takefocus=0)
            b_x.pack(side="left", pady=3)
            add_tip(b_x, "إخفاء شريط التحديث لهذه الجلسة فقط")
        else:
            tk.Label(bar, text="راجع المدير", bg=upd_bg, fg="#a16207",
                     font=("Segoe UI", 9, "bold")).pack(side="left", padx=(12, 4))
        self.update_bar = bar

    def dismiss_update_bar(self):
        """(2) زر ✕: إخفاء شريط الإشعار لهذه الجلسة فقط (يعود مع تشغيل جديد)"""
        self.update_bar_dismissed = True
        # ★ إضافة (إصلاح 1): تذكر رقم إصدار الشريط المخفي — لا يعود الشريط
        # في نفس الجلسة إلا إذا اكتشف الفحص رقماً أحدث منه فعلياً
        self.update_bar_dismissed_version = getattr(
            self, "update_available_version", None)
        if getattr(self, "update_bar", None) is not None:
            try:
                self.update_bar.destroy()
            except Exception:
                pass
            self.update_bar = None

    def update_now_dialog(self):
        """(3) نافذة التحديث — للمدير فقط: «يتوفر تحديث جديد — يتطلب إعادة
        تشغيل بعد التثبيت. التحديث لا يلمس بياناتك والتقارير نهائياً.
        تثبيت الآن؟» + زر «🔄 فحص التحديثات الآن»، وعند التثبيت تُنفّذ
        الخطوات الصارمة بالترتيب مع إلغاء آمن عند أي فشل"""
        if not self.require_admin("manager"):
            return
        win = self.register_window(tk.Toplevel(self))
        win.title("تحديث البرنامج")
        win.geometry("460x310")
        win.resizable(False, False)
        win.configure(bg=CARD)
        win.transient(self)
        try:
            win.grab_set()
        except Exception:
            pass
        tk.Label(win, text="⬇️", bg=CARD, fg=DARK, font=("Segoe UI", 26)).pack(pady=(14, 0))
        lbl = tk.Label(win, text="", bg=CARD, fg=DARK, font=FT,
                       wraplength=400, justify="center")
        lbl.pack(pady=(4, 2))
        tk.Label(win, text="يتطلب إعادة تشغيل بعد التثبيت.\n"
                           "التحديث لا يلمس بياناتك والتقارير نهائياً.",
                 bg=CARD, fg=GRAY, font=("Segoe UI", 10),
                 justify="center").pack(pady=(0, 8))
        fr_btns = tk.Frame(win, bg=CARD)
        fr_btns.pack(pady=2)
        b_install = self.mk_btn(fr_btns, "تثبيت الآن",
                                lambda: self.update_install(win, b_install, lbl), GREEN)
        b_install.pack(side="right", padx=6)
        add_tip(b_install, "تنزيل الإصدار الجديد وتثبيته — لا يلمس البيانات والتقارير نهائياً")
        b_close = self.mk_btn(fr_btns, "إغلاق", win.destroy, "#475569")
        b_close.pack(side="right", padx=6)
        b_recheck = self.mk_btn(win, "🔄 فحص التحديثات الآن",
                                lambda: self.update_check_now(win, lbl, b_install, b_close), "#0369a1")
        b_recheck.pack(pady=(10, 12))
        add_tip(b_recheck, "إعادة فحص التحديثات الآن بغض النظر عن الفحص التلقائي الصامت")
        # ★ إضافة (نافذة «عن البرنامج»): زر داخل نافذة التحديث بجانب زر الفحص —
        # يفتح نبذة مختصرة عن البرنامج (قراءة فقط من المتغيرات والجداول
        # القائمة بلا أي فحص شبكي عند الفتح)
        b_about = self.mk_btn(win, "ℹ️ عن البرنامج", self.about_dialog, "#475569")
        b_about.pack(pady=(0, 12))
        add_tip(b_about, "نبذة عن البرنامج: الإصدار وآخر تحديث ومجلد البيانات — بلا أي اتصال")
        # الحالة الابتدائية: إصدار معروف من الفحص الصامت، أو فحص فوري عند الفتح
        ver = getattr(self, "update_available_version", None)
        if ver:
            lbl.config(text=f"يتوفر تحديث جديد (الإصدار {ver})", fg=ORANGE)
        else:
            # ★ إصلاح (11 — البند د): بلا إصدار مؤكد يبدأ الفحص فوراً وزر
            # «تثبيت الآن» مخفي حتى تثبت نتيجة المقارنة وجود إصدار أحدث فعلياً
            self.update_check_now(win, lbl, b_install, b_close)

    def update_check_now(self, win, lbl, install_btn=None, anchor_btn=None):
        """(4) زر «🔄 فحص التحديثات الآن»: فحص فوري بنفس مهلة الفحص الصامت —
        يحدّث حالة نافذة التحديث وشريط الإشعار الأصفر معاً وبهدوء عند الفشل
        ★ إصلاح (11 — البند د): عند عدم وجود إصدار أحدث فعلياً تظهر رسالة
        «✅ أنت على أحدث إصدار — الإصدار الحالي [VERSION]» ولا يظهر أي زر
        تثبيت في هذه الحالة — فزر «تثبيت الآن» يُخفى فور بدء الفحص ولا
        يُعاد إظهاره إلا من داخل نتيجة مقارنة ناجحة تثبت إصداراً أحدث"""
        def _hide_install():
            if install_btn is not None:
                try:
                    install_btn.pack_forget()
                except Exception:
                    pass
        def _show_install():
            if install_btn is not None:
                try:
                    install_btn.pack(side="right", padx=6, before=anchor_btn)
                except Exception:
                    install_btn.pack(side="right", padx=6)
        try:
            lbl.config(text="جارٍ الفحص...", fg=GRAY)
        except Exception:
            pass
        _hide_install()      # مخفي أثناء الفحص وفي كل نتيجة ليست «إصداراً أحدث»
        box = update_fetch_async(UPDATE_VERSION_URL, UPDATE_CHECK_TIMEOUT)
        def _poll():
            if box["state"] != "done":
                try:
                    win.after(250, _poll)
                except Exception:
                    pass
                return
            remote = update_parse_version(box["data"] or b"")
            try:
                if remote is None:
                    lbl.config(text="تعذر فحص التحديثات الآن", fg=RED)
                    return
                if not update_is_newer(remote, VERSION):
                    self.update_available_version = None  # لا تحديث مؤكد الآن
                    self.refresh_update_bar()             # إخفاء الشريط والزر إن بقيا من تأكيد سابق
                    lbl.config(text=f"✅ أنت على أحدث إصدار — الإصدار الحالي {VERSION}",
                               fg=GREEN)
                    return
                self.update_available_version = remote
                audit("فحص تحديث يدوي", f"يتوفر إصدار جديد: {remote}")
                lbl.config(text=f"يتوفر تحديث جديد (الإصدار {remote})", fg=ORANGE)
                _show_install()
                self.refresh_update_bar()
            except Exception:
                pass
        try:
            win.after(250, _poll)
        except Exception:
            pass

    def update_check_manual(self, btn=None):
        """★ إضافة (إصلاح 3 — البندان أ+ب): «🔄 فحص التحديثات الآن» من
        الشريط الأصفر أو من قائمة المستخدم — فحص يدوي فوري برسالة نتيجة
        عربية دائماً: «🔔 يتوفر تحديث جديد — الإصدار [رقم]» مع ظهور الشريط،
        أو «✅ أنت على أحدث إصدار — الإصدار الحالي [VERSION]»، أو «⚠ تعذر
        الاتصال — تحقق من الإنترنت وحاول لاحقاً» عند فشل الاتصال — ونص زر
        الفحص «جارٍ الفحص...» أثناء الفحص ثم يعود لسابقه، وكل فحص يدوي
        ونتيجته في سجل التدقيق"""
        if getattr(self, "_manual_check_busy", False):
            return                      # فحص جارٍ فعلاً — لا ضغط مزدوج
        self._manual_check_busy = True
        old_text = None
        if btn is not None:             # نص الزر «جارٍ الفحص...» ثم يعود
            try:
                old_text = btn.cget("text")
                btn.config(text="جارٍ الفحص...", state="disabled", cursor="watch")
            except Exception:
                btn = None

        def _restore():
            """إعادة زر الفحص لنصه وحالته (بأقصى جهد إن كان الشريط أعيد
            بناؤه أثناء الفحص) ثم السماح بفحص جديد"""
            if btn is not None and old_text:
                try:
                    btn.config(text=old_text, state="normal", cursor="hand2")
                except Exception:
                    pass
            self._manual_check_busy = False

        box = update_fetch_async(UPDATE_VERSION_URL, UPDATE_CHECK_TIMEOUT)

        def _poll():
            if box["state"] != "done":
                try:
                    self.after(250, _poll)
                except Exception:
                    _restore()
                return
            remote = update_parse_version(box["data"] or b"")
            _restore()                  # الزر يعود لسابقه قبل رسالة النتيجة
            if remote is None:          # فشل الاتصال
                audit("فحص تحديث يدوي", "تعذر الاتصال — فحص فاشل")
                messagebox.showwarning("فحص التحديثات",
                    "⚠ تعذر الاتصال — تحقق من الإنترنت وحاول لاحقاً", parent=self)
                return
            if not update_is_newer(remote, VERSION):
                self.update_available_version = None   # لا تحديث مؤكد الآن
                self.update_last_check_result = "latest"
                self.refresh_update_bar()   # إخفاء الشريط والزر إن بقيا من تأكيد سابق
                audit("فحص تحديث يدوي", f"أحدث إصدار ({VERSION})")
                messagebox.showinfo("فحص التحديثات",
                    f"✅ أنت على أحدث إصدار — الإصدار الحالي {VERSION}", parent=self)
                return
            self.update_available_version = remote     # تحديث مؤكد → الشريط فوراً
            self.update_last_check_result = "available"
            self.refresh_update_bar()
            audit("فحص تحديث يدوي", f"يتوفر إصدار جديد: {remote}")
            messagebox.showinfo("فحص التحديثات",
                f"🔔 يتوفر تحديث جديد — الإصدار {remote}", parent=self)

        try:
            self.after(250, _poll)
        except Exception:
            _restore()

    def _update_periodic_check(self):
        """★ إضافة (إصلاح 1 — الفحص الدوري): كل 30 دقيقة فحص صامت بنفس دالة
        الفحص القائمة — عند اكتشاف إصدار أحدث يظهر الشريط الأصفر فوراً دون
        إعادة تشغيل ولكل الأدوار، وبلا تحديث صمت تام (لا رسائل ولا أي أثر
        إطلاقاً)، ثم يُعيد جدولة نفسه ما دام البرنامج مفتوحاً"""
        try:
            update_check_silent(self, quiet=True)
        except Exception:
            pass
        try:
            self._update_periodic_after_id = self.after(
                30 * 60 * 1000, self._update_periodic_check)
        except Exception:
            pass          # البرنامج أُغلق — يتوقف المؤقت بهدوء

    def update_install(self, win, btn, lbl):
        """(3) خطوات التثبيت الصارمة بالترتيب: (أ) تنزيل إلى ملف مؤقت
        main_new.tmp وليس فوق القديم ← (ب) التحقق من السلامة: حجم أكبر من
        10 كيلوبايت + يحتوي VERSION + يبدأ بتعليق أو import ← (ج) حفظ
        النسخة القديمة في أرشيف الإصدارات versions_archive باسم منظم
        main_v[الإصدار]_[التاريخ].py — سجل تاريخي كامل لا يُحذف منه شيء
        (★ التعديل المصرح به الوحيد في خطوات التثبيت) ← (د)
        الاستبدال باسم مكتشف ديناميكياً من __file__ ← (هـ) حفظ
        last_update_date + سجل التدقيق ← (و) رسالة إعادة التشغيل وزر
        «إغلاق الآن» — ولو البرنامج EXE فالتحديث يدوي — وأي فشل في أي
        خطوة = إلغاء آمن برسالة «لم يتغير شيء»"""
        # نسخة EXE لا تُحدَّث تلقائياً: تنبيه صريح دون أي تنزيل
        if getattr(sys, "frozen", False):
            messagebox.showinfo("تحديث EXE",
                "التحديث التلقائي لنسخة Python — حدث EXE يدوياً", parent=win)
            return
        # اسم ملف البرنامج يُكتشف ديناميكياً من __file__ (وليس اسماً ثابتاً)
        try:
            target = os.path.abspath(__file__)
        except Exception:
            target = None
        if not target or not os.path.isfile(target):
            messagebox.showerror("فشل التحديث",
                "تعذر تحديد موقع ملف البرنامج — لم يتغير شيء، حاول لاحقاً", parent=win)
            return
        tmp = os.path.join(os.path.dirname(target), "main_new.tmp")   # (أ) بجانب البرنامج
        btn.config(text="⬇️ جارٍ التنزيل...", state="disabled", cursor="watch")
        try:
            lbl.config(text="جارٍ تنزيل التحديث...", fg=GRAY)
        except Exception:
            pass
        box = update_fetch_async(UPDATE_FILE_URL, UPDATE_DOWNLOAD_TIMEOUT)

        def _fail(msg):
            """إلغاء آمن: حذف الملف المؤقت إن وُجد وإعادة الزر — لم يتغير شيء
            (بأقصى جهد إن كانت النافذة أُغلقت أثناء التنزيل)"""
            try:
                os.remove(tmp)
            except Exception:
                pass
            try:
                btn.config(text="تثبيت الآن", state="normal", cursor="hand2")
                lbl.config(text="يتوفر تحديث جديد (الإصدار "
                          + str(getattr(self, "update_available_version", "")) + ")",
                          fg=ORANGE)
            except Exception:
                pass
            try:
                messagebox.showerror("فشل التحديث", msg, parent=win)
            except Exception:
                pass

        def _poll():
            if box["state"] != "done":
                try:
                    win.after(250, _poll)
                except Exception:
                    pass
                return
            # (أ) التنزيل إلى الملف المؤقت — وليس فوق الملف القديم
            data = box["data"]
            if data is None:
                _fail("فشل التنزيل — لم يتغير شيء، حاول لاحقاً"); return
            try:
                with open(tmp, "wb") as f:
                    f.write(data)
            except Exception:
                _fail("فشل حفظ ملف التحديث — لم يتغير شيء، حاول لاحقاً"); return
            # (ب) التحقق من سلامة الملف المؤقت قبل أي مساس بالملف القديم:
            # حجم > 10 كيلوبايت + يحتوي VERSION + يبدأ بتعليق أو import
            ok = False
            try:
                with open(tmp, "rb") as f:
                    blob = f.read()
                first = next((ln.strip() for ln in blob.splitlines() if ln.strip()), b"")
                ok = (len(blob) > 10 * 1024 and b"VERSION" in blob
                      and (first.startswith(b"#") or first.startswith(b"import")
                           or first.startswith(b"from") or first.startswith(b'"""')))
            except Exception:
                ok = False
            if not ok:
                _fail("فشل التنزيل — لم يتغير شيء، حاول لاحقاً"); return
            # (ج) ★ تعديل مصرح به (أرشيف الإصدارات): حفظ النسخة القديمة في
            # مجلد أرشيف الإصدارات versions_archive باسم منظم
            # main_v[الإصدار]_[التاريخ].py بدل نسخ main_backup_* بجوار
            # البرنامج — الأرشيف سجل تاريخي كامل لا يُحذف منه أي ملف
            # تلقائياً أبداً (بدل قاعدة آخر 3)، وفشل الحفظ يلغي التحديث
            # بأمان كما كان تماماً، وبقية الخطوات (أ/ب/د/هـ/و) كما هي حرفياً
            saved_archive = archive_save_current()
            if saved_archive is None:
                _fail("تعذر إنشاء نسخة الأمان — لم يتغير شيء، حاول لاحقاً"); return
            audit("أرشيف الإصدارات",
                  f"حُفظ الإصدار {VERSION} في الأرشيف قبل التحديث إلى "
                  + str(getattr(self, "update_available_version", "إصدار جديد")))
            # (د) الاستبدال — بعد نجاح كل الفحوص أعلاه فقط
            try:
                os.replace(tmp, target)
            except Exception:
                _fail("فشل استبدال ملف البرنامج — لم يتغير شيء، حاول لاحقاً"); return
            # (هـ) حفظ last_update_date في الإعدادات + سجل التدقيق (بأقصى جهد)
            try:
                set_setting("last_update_date",
                            datetime.now().strftime("%Y-%m-%d %H:%M"))
                audit("تحديث البرنامج",
                      f"من {VERSION} إلى {getattr(self, 'update_available_version', 'إصدار جديد')}")
            except Exception:
                pass
            # (و) رسالة النجاح + زر «إغلاق الآن» — يكتمل التحديث بإعادة التشغيل
            try:
                for w in win.winfo_children():
                    w.destroy()
                tk.Label(win, text="تم التحديث ✅", bg=CARD, fg=GREEN,
                         font=FT).pack(pady=(36, 6))
                tk.Label(win, text="أغلق البرنامج وافتحه من جديد.", bg=CARD, fg=DARK,
                         font=F).pack(pady=(0, 14))
                self.mk_btn(win, "إغلاق الآن", self.exit_app, RED).pack(ipadx=10)
            except Exception:
                pass
        try:
            win.after(250, _poll)
        except Exception:
            pass

    def about_dialog(self):
        """★ إضافة (نافذة «عن البرنامج»): نبذة مختصرة أنيقة عن البرنامج بأسلوب
        نافذة تسجيل الدخول القائمة (بطاقة فاتحة وسطية فوق خلفية داكنة) — قراءة
        فقط من المتغيرات والجداول القائمة بلا أي فحص شبكي عند الفتح: الإصدار
        الحالي، آخر تحديث ناجح من الإعدادات، حالة آخر فحص تحديث (ذاكرة الجلسة
        ثم سجل التدقيق القائم)، تاريخ اليوم وساعة حية تتحدث كل ثانية، مستخدم
        الجلسة، ومجلد البيانات بخط صغير قابل للتحديد مع زر نسخ 📋 للمحفظة"""
        win = self.register_window(tk.Toplevel(self))
        win.title("عن البرنامج")
        # ★ إصلاح (2): رفع الارتفاع 520 ← 560 فقط — صف «الإصدارات المحفوظة
        # بالأرشيف» الجديد يحتاج مساحته دون قصّ أي عنصر قائم
        W, H = 420, 560
        sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
        win.geometry(f"{W}x{H}+{(sw - W) // 2}+{max((sh - H) // 2 - 40, 0)}")
        win.resizable(False, False)
        win.configure(bg=SIDEBAR)
        win.transient(self)
        try:
            win.grab_set()
        except Exception:
            pass

        # ---------- عناصر الأسفل تُرصّ أولاً كي تثبت في مكانها ----------
        # زر «إغلاق» رمادي داكن أسفل النافذة (نفس رمادي أزرار الإغلاق القائمة)
        self.mk_btn(win, "إغلاق", win.destroy, "#475569").pack(side="bottom",
                                                                pady=(4, 16))
        # سطر صغير رمادي: البيانات محلية مع نسخ احتياطية تلقائية
        tk.Label(win, text="البيانات محفوظة محلياً مع نسخ احتياطية تلقائية 🔒",
                 bg=SIDEBAR, fg="#94a3b8",
                 font=("Segoe UI", 9)).pack(side="bottom", pady=(2, 2))
        # الفاصل الثاني (تحت البطاقة)
        tk.Frame(win, bg="#334155", height=1).pack(side="bottom", fill="x",
                                                   padx=46, pady=(6, 4))

        # ---------- الرأس: أيقونة كبيرة + اسم البرنامج + السطر الفرعي ----------
        tk.Label(win, text="🖥️", bg=SIDEBAR, fg="#e2e8f0",
                 font=("Segoe UI", 30)).pack(pady=(18, 2))
        tk.Label(win, text="نظام المبيعات والمرتجعات", bg=SIDEBAR, fg="#f1f5f9",
                 font=FT).pack(pady=(0, 2))
        tk.Label(win, text="برنامج إدارة محل الكمبيوتر", bg=SIDEBAR, fg="#94a3b8",
                 font=("Segoe UI", 10)).pack(pady=(0, 8))
        # الفاصل الأول اللطيف (بلون أهدأ من الخلفية الداكنة)
        tk.Frame(win, bg="#334155", height=1).pack(fill="x", padx=46, pady=(2, 4))

        # ---------- بطاقة المعلومات الفاتحة (CARD بإطار BORDER) ----------
        card = tk.Frame(win, bg=CARD, highlightbackground=BORDER,
                        highlightthickness=1)
        card.pack(fill="both", expand=True, padx=26, pady=(0, 6))

        def info_row(title, value="", value_fg=DARK, value_font=F):
            """صف معلومة داخل البطاقة: العنوان يميناً والقيمة يساراً بخط واضح"""
            fr = tk.Frame(card, bg=CARD)
            fr.pack(fill="x", padx=14, pady=6)
            tk.Label(fr, text=title, bg=CARD, fg=GRAY,
                     font=("Segoe UI", 10, "bold"), anchor="e").pack(side="right")
            lbl = tk.Label(fr, text=value, bg=CARD, fg=value_fg,
                           font=value_font, anchor="w")
            lbl.pack(side="left")
            return lbl

        # (1) الإصدار الحالي
        info_row("الإصدار الحالي:", str(VERSION), DARK, FB)

        # (2) آخر تحديث ناجح — من الإعدادات القائمة فقط (بلا أي اتصال)
        try:
            last_upd = get_setting("last_update_date") or "لم يتم تحديث بعد"
        except Exception:
            last_upd = "لم يتم تحديث بعد"
        info_row("آخر تحديث ناجح:", last_upd,
                 DARK if last_upd != "لم يتم تحديث بعد" else GRAY)

        # (3) حالة التحديث — من نتيجة آخر فحص فقط (بلا فحص شبكي جديد): إصدار
        # مؤكد بذاكرة الجلسة = «يتوفر تحديث جديد»، وإلا نتيجة آخر فحص مسجلة
        # في سجل التدقيق القائم («أحدث إصدار») — وإن لم يُجرَ فحص قط أو فشل
        # الفحص الأخير = «—»
        # ★ إصلاح (2): نتيجة آخر فحص من متغير الذاكرة أولاً (الفحص الدوري
        # لا يكتب في سجل التدقيق عند غياب تحديث — صمت تام) والنصان
        # الموحدان: «أحدث إصدار ✅» / «يتوفر تحديث جديد 🔔»
        if getattr(self, "update_available_version", None):
            state_txt, state_fg = "يتوفر تحديث جديد 🔔", ORANGE
        elif getattr(self, "update_last_check_result", None) == "latest":
            state_txt, state_fg = "أحدث إصدار ✅", GREEN
        else:
            state_txt, state_fg = "—", GRAY
            try:
                with connect() as conn:
                    r = conn.execute(
                        "SELECT details FROM audit_log WHERE action IN "
                        "('فحص تحديث تلقائي', 'فحص تحديث يدوي') "
                        "ORDER BY id DESC LIMIT 1").fetchone()
                if r and "أحدث إصدار" in str(r["details"]):
                    state_txt, state_fg = "أحدث إصدار ✅", GREEN
            except Exception:
                pass
        info_row("حالة التحديث:", state_txt, state_fg)

        # ★ إضافة (أرشيف الإصدارات — نقطة ربط): عدد الإصدارات المحفوظة
        # في الأرشيف — يُحسب من ملفات versions_archive فقط (بلا أي اتصال)
        try:
            arch_n = archive_count()
        except Exception:
            arch_n = 0
        info_row("الإصدارات المحفوظة بالأرشيف:", str(arch_n),
                 DARK if arch_n else GRAY)

        # (4) تاريخ اليوم والوقت — ساعة حية تتحدث كل ثانية بـ after
        lbl_clock = info_row("تاريخ اليوم والوقت:", "", DARK, ("Segoe UI", 10))

        def _tick():
            try:
                if not win.winfo_exists():
                    return
                now = datetime.now()
                d = now.strftime("%Y-%m-%d")
                lbl_clock.config(text=f"{day_name(d)} — {d} "
                                      + now.strftime("%H:%M:%S"))
                win.after(1000, _tick)
            except Exception:
                pass
        _tick()

        # (5) مستخدم الجلسة
        info_row("مستخدم الجلسة:",
                 f"{getattr(self, 'user_name', '—')} "
                 f"({getattr(self, 'role', '—')})")

        # (6) مجلد البيانات — عنوان يميناً ثم المسار بخط صغير قابل للتحديد
        fr_d = tk.Frame(card, bg=CARD)
        fr_d.pack(fill="x", padx=14, pady=(6, 0))
        tk.Label(fr_d, text="مجلد البيانات:", bg=CARD, fg=GRAY,
                 font=("Segoe UI", 10, "bold"), anchor="e").pack(side="right")
        fr_p = tk.Frame(card, bg=CARD)
        fr_p.pack(fill="x", padx=14, pady=(2, 8))
        e_path = tk.Entry(fr_p, font=("Segoe UI", 8), justify="center",
                          relief="solid", bd=1)
        e_path.insert(0, data_dir())
        e_path.configure(state="readonly")   # للقراءة فقط — قابل للتحديد والنسخ
        e_path.pack(side="right", fill="x", expand=True)

        def _copy_done():
            """إعادة زر النسخ لشكله بعد رسالة التأكيد القصيرة (بأقصى جهد)"""
            try:
                b_copy.config(text="📋", state="normal")
            except Exception:
                pass

        def _copy_path():
            """نسخ مسار مجلد البيانات إلى المحفظة مع رسالة تأكيد قصيرة"""
            try:
                win.clipboard_clear()
                win.clipboard_append(e_path.get())
                b_copy.config(text="✅ تم النسخ", state="disabled")
                win.after(1500, _copy_done)
            except Exception:
                pass
        b_copy = tk.Button(fr_p, text="📋", command=_copy_path, bg=CARD, fg=DARK,
                           font=("Segoe UI", 10), bd=1, relief="solid",
                           cursor="hand2", padx=6, pady=2)
        b_copy.pack(side="left", padx=(0, 6))

    def archive_open_folder(self):
        """★ إضافة (أرشيف الإصدارات): زر «📂 فتح مجلد الأرشيف» — يفتح مجلد
        versions_archive في مستكشف ملفات ويندوز بنفس نمط زر «فتح مجلد
        النسخ» القائم تماماً"""
        try:
            folder = archive_dir()
            if os.name == "nt":
                os.startfile(folder)
            else:
                messagebox.showinfo("مجلد أرشيف الإصدارات", folder)
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("خطأ", f"تعذر فتح مجلد الأرشيف:\n{e}")

    def archive_versions_dialog(self):
        """★ إضافة (أرشيف الإصدارات): نافذة عرض أرشيف الإصدارات — للمدير
        فقط: جدول بكل ملفات الأرشيف مرتبة من الأحدث (الاسم | الإصدار |
        تاريخ الحفظ | الحجم بالكيلوبايت) + زر فتح مجلد الأرشيف في مستكشف
        ويندوز + زر استعادة أي إصدار بتحذير قوي (تُحفظ النسخة الحالية في
        الأرشيف أولاً بنفس التسمية قبل أي استبدال — لا فقدان في أي اتجاه)
        — وكل إجراء في سجل التدقيق"""
        if not self.require_admin("manager"):
            return
        win = self.register_window(tk.Toplevel(self))
        win.title("أرشيف الإصدارات")
        W, H = 780, 520
        sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
        win.geometry(f"{W}x{H}+{max((sw - W) // 2, 0)}+{max((sh - H) // 2 - 30, 0)}")
        win.resizable(False, False)
        win.configure(bg=CARD)
        win.transient(self)
        try:
            win.grab_set()
        except Exception:
            pass
        # الرأس بنمط عناوين الشاشات القائم
        tk.Label(win, text="🗃️", bg=CARD, fg=DARK,
                 font=("Segoe UI", 24)).pack(pady=(12, 0))
        tk.Label(win, text="أرشيف الإصدارات", bg=CARD, fg=DARK, font=FT).pack()
        tk.Label(win, text="سجل تاريخي كامل لكل إصدارات البرنامج المحفوظة — لا يُحذف منه شيء تلقائياً",
                 bg=CARD, fg=GRAY, font=("Segoe UI", 10)).pack(pady=(0, 4))
        # جدول الملفات مرتباً من الأحدث إلى الأقدم
        frm, tv = self.mk_tree(win, ["الاسم", "الإصدار", "تاريخ الحفظ", "الحجم (KB)"],
                               [340, 90, 150, 90])
        frm.pack(fill="both", expand=True, padx=18, pady=6)
        self._archive_rows = []          # مسارات ملفات الأرشيف بترتيب الصفوف
        lbl_count = tk.Label(win, text="", bg=CARD, fg=GRAY, font=("Segoe UI", 10))
        lbl_count.pack(pady=(2, 0))

        def load_rows():
            """قراءة ملفات الأرشيف من جديد وملء الجدول من الأحدث"""
            tv.delete(*tv.get_children())
            self._archive_rows = []
            rows = archive_list_files()          # مرتبة من الأحدث
            for r in rows:
                tv.insert("", "end", values=(r["name"], r["version"],
                                             r["saved"], r["size_kb"]))
                self._archive_rows.append(r["path"])
            lbl_count.config(text=f"عدد الإصدارات المحفوظة: {len(rows)}")
        load_rows()
        # الأزرار: الاستعادة (الأساسي) ثم فتح المجلد ثم التحديث ثم الإغلاق
        fr_btns = tk.Frame(win, bg=CARD)
        fr_btns.pack(pady=(4, 12))
        b_restore = self.mk_btn(fr_btns, "♻️ استعادة هذا الإصدار",
                                lambda: self.archive_restore_selected(tv, win, load_rows), ORANGE)
        b_restore.pack(side="right", padx=6)
        add_tip(b_restore, "استبدال كود البرنامج الحالي بالنسخة المختارة — "
                           "تُحفظ النسخة الحالية في الأرشيف أولاً ثم رسالة إعادة التشغيل")
        b_open = self.mk_btn(fr_btns, "📂 فتح مجلد الأرشيف",
                             self.archive_open_folder, "#0369a1")
        b_open.pack(side="right", padx=6)
        add_tip(b_open, "فتح مجلد أرشيف الإصدارات في مستكشف ملفات ويندوز")
        b_refresh = self.mk_btn(fr_btns, "🔄 تحديث", load_rows, "#475569")
        b_refresh.pack(side="right", padx=6)
        add_tip(b_refresh, "إعادة قراءة ملفات الأرشيف من جديد")
        b_close = self.mk_btn(fr_btns, "إغلاق", win.destroy, "#475569")
        b_close.pack(side="right", padx=6)
        add_tip(b_close, "إغلاق نافذة أرشيف الإصدارات")

    def archive_restore_selected(self, tv, win, reload_rows):
        """★ إضافة (أرشيف الإصدارات): زر «♻️ استعادة هذا الإصدار» — تحذير
        قوي بالعربية أن الاستعادة تستبدل كود البرنامج الحالي، ثم تُحفظ
        النسخة الحالية في الأرشيف أولاً بنفس التسمية المنظمة (لا فقدان في
        أي اتجاه) قبل استبدال ملف البرنامج بنسخة من الأرشيف (نسخاً لا
        نقلاً — الأرشيف لا يفقد شيئاً) + رسالة إعادة التشغيل + تسجيل كامل
        في سجل التدقيق (من استعاد أي إصدار ومتى)"""
        sel = tv.selection()
        if not sel:
            messagebox.showinfo("تنبيه", "اختر إصداراً من الجدول أولاً", parent=win)
            return
        try:
            i = tv.index(sel[0])              # رقم الصف المختار في الجدول
            path = self._archive_rows[i]
        except Exception:
            return
        name = os.path.basename(path)
        ver = archive_file_version(path)
        # نسخة EXE لا تُستعاد تلقائياً: تنبيه يدوي دون أي مساس بالملف
        if getattr(sys, "frozen", False):
            messagebox.showinfo("استعادة EXE",
                "الاستعادة التلقائية لنسخة Python — حدّث EXE يدوياً", parent=win)
            return
        # تحذير قوي بالعربية (تأكيد مزدوج) — الاستعادة تستبدل الكود الحالي
        warn = ("⚠️ تحذير هام ⚠️\n\n"
                "الاستعادة ستستبدل كود البرنامج الحالي بالكامل بالنسخة المختارة:\n"
                f"{name}  (الإصدار {ver})\n\n"
                "ستفقد كل تحسينات الإصدارات الأحدث من هذا الإصدار.\n"
                "سيُحفظ الكود الحالي أولاً في الأرشيف تلقائياً قبل الاستبدال — "
                "لا فقدان في أي اتجاه.\n"
                "بياناتك وتقاريرك لا تُمس نهائياً (محفوظة في قاعدة بيانات منفصلة).\n\n"
                "هل أنت متأكد من المتابعة؟")
        if not messagebox.askyesno("تأكيد الاستعادة (1 من 2)", warn, parent=win):
            return
        if not messagebox.askyesno("تأكيد الاستعادة (2 من 2)",
                "تأكيد أخير:\nهل تريد فعلاً استبدال كود البرنامج الحالي بهذه النسخة الآن؟",
                parent=win):
            return
        # 1) حفظ الكود الحالي في الأرشيف أولاً — بنفس التسمية المنظمة
        saved = archive_save_current()
        if saved is None:
            messagebox.showerror("فشلت الاستعادة",
                "تعذر حفظ النسخة الحالية في الأرشيف قبل الاستعادة —\n"
                "لم يتغير شيء إطلاقاً، حاول لاحقاً.", parent=win)
            return
        # 2) الاستبدال بنسخة من ملف الأرشيف (نسخ لا نقل — الأرشيف لا يفقد شيئاً)
        try:
            target = os.path.abspath(__file__)
            if not os.path.isfile(target):
                raise Exception("تعذر تحديد موقع ملف البرنامج")
            shutil.copy2(path, target)
        except Exception as e:
            log_error(e, sys.exc_info()[2])
            messagebox.showerror("فشلت الاستعادة",
                "تعذر استبدال ملف البرنامج:\n" + str(e) +
                "\n\nلم يتغير شيء (راجع error_log.txt).", parent=win)
            return
        # 3) تسجيل كامل في سجل التدقيق + رسالة إعادة التشغيل
        audit("أرشيف الإصدارات",
              f"استعادة إصدار {ver} ({name}) — حُفظ الكود الحالي أولاً باسم "
              + os.path.basename(saved))
        try:
            reload_rows()
        except Exception:
            pass
        messagebox.showinfo("تمت الاستعادة ✅",
            "استُبدل كود البرنامج بالنسخة المختارة بنجاح.\n"
            "حُفظ الكود السابق في الأرشيف باسم:\n" + os.path.basename(saved) +
            "\n\n⚠ أغلق البرنامج الآن وافتحه من جديد لتفعيل الإصدار المستعاد.",
            parent=win)
        self.exit_app()      # إغلاق البرنامج — يجب إعادة تشغيله بعد الاستعادة


# ═══════════════════════════════════════════════════════════
# ★★★ (إصدار 3 — ميزة 2) نافذة تسجيل الدخول بالحسابات قبل فتح البرنامج ★★★
# ═══════════════════════════════════════════════════════════
# ═══════════════════════════════════════════════════════════
# ★★★ إضافات الإصدار 9 — نافذة تسجيل الدخول المحسّنة (الميزات الثماني) ★★★
# التعديل المصرح به الوحيد في هذه الجلسة: إعادة بناء كود بناء نافذة الدخول
# الحالية — login_flow ودوالها الداخلية + login_dialog — بنفس منطق التحقق
# الحالي تماماً (نفس رسائل الخطأ الثلاثة، نفس تسجيل audit_log للمحاولات
# الفاشلة، نفس شرط active=1، نفس شاشة إنشاء حساب المدير أول مرة)
# ═══════════════════════════════════════════════════════════

LOGIN_W, LOGIN_H = 420, 520      # ★ مقاس نافذة الدخول الجديدة (بلا إطار ويندوز)

def pw_strength_info(pw):
    """★ إضافة (إصدار 9 — الميزة 4): قوة كلمة المرور — (اللون، النص، المستوى):
    أحمر «ضعيفة» أقل من 5 أحرف / برتقالي «متوسطة» 5 أحرف فأكثر /
    أخضر «قوية» 6 أحرف فأكثر وفيها رقم على الأقل"""
    if len(pw) < 5:
        return RED, "ضعيفة", "weak"
    if len(pw) >= 6 and any(ch.isdigit() for ch in pw):
        return GREEN, "قوية", "strong"
    return ORANGE, "متوسطة", "medium"

def pw_is_weak(pw):
    """★ إضافة (إصدار 9 — الميزة 4): كلمة مرور ضعيفة جداً (أحمر) — تمنع الحفظ
    في شاشة إنشاء المدير ونافذة تغيير كلمة المرور برسالة عربية واضحة"""
    return pw_strength_info(pw)[2] == "weak"

def make_strength_bar(parent):
    """★ إضافة (إصدار 9 — الميزة 4): شريط قوة كلمة المرور + النص الإرشادي
    بجانبه — يُعبّأ في مكان الاستدعاء ويرجع دالة update(pw) تُنادى عند كل
    ضغطة مفتاح: يتغير اللون والنص (ضعيفة / متوسطة / قوية) فوراً"""
    row = tk.Frame(parent, bg=CARD)
    row.pack(fill="x", padx=18, pady=(6, 0))
    track = tk.Frame(row, bg=BORDER, height=7)
    track.pack(side="right", fill="x", expand=True)
    track.pack_propagate(False)
    lbl = tk.Label(row, text="قوة كلمة المرور", bg=CARD, fg=GRAY,
                   font=("Segoe UI", 9, "bold"), anchor="e")
    lbl.pack(side="right", padx=(0, 10))
    hints = {"weak": "أقل من 5 أحرف", "medium": "5 أحرف فأكثر", "strong": "6+ أحرف وفيها رقم"}
    def update(pw):
        """يتحدث مع كل ضغطة مفتاح — والفراغ يعيد الحالة الرمادية الأولى"""
        if not pw:
            track.config(bg=BORDER)
            lbl.config(text="قوة كلمة المرور", fg=GRAY)
            return
        color, txt, level = pw_strength_info(pw)
        track.config(bg=color)
        lbl.config(text=f"قوة كلمة المرور: {txt} ({hints[level]})", fg=color)
    return update

def add_eye_to_entry(entry):
    """★ إضافة (إصدار 9 — الميزة 1): زر عين 👁 صغير داخل حقل كلمة المرور
    (على يساره) — يبدّل الإظهار/الإخفاء: 👁 عند الإخفاء و🙈 عند الإظهار،
    ويعود للإخفاء تلقائياً بعد 5 ثوانٍ. لا يغيّر أي شيء آخر في الحقل"""
    state = {"after_id": None, "mask": entry.cget("show") or "•"}

    def _hide():
        try:
            entry.config(show=state["mask"])
            btn.config(text="👁")
        except Exception:
            pass
        state["after_id"] = None

    def _toggle():
        try:
            shown = str(entry.cget("show")) == ""     # الحقل معروض الآن؟
            if state["after_id"] is not None:
                try:
                    entry.after_cancel(state["after_id"])
                except Exception:
                    pass
                state["after_id"] = None
            if shown:
                _hide()                              # كان معروضاً → عُد للإخفاء
            else:
                entry.config(show="")
                btn.config(text="🙈")
                state["after_id"] = entry.after(5000, _hide)   # إخفاء تلقائي بعد 5 ثوانٍ
        except Exception:
            pass

    btn = tk.Button(entry.master, text="👁", command=_toggle, bg=CARD, fg=GRAY,
                    font=("Segoe UI", 10), bd=0, relief="flat", cursor="hand2",
                    activebackground=CARD, activeforeground=ACCENT, takefocus=0)
    btn.place(in_=entry, x=1, y=1, relheight=1.0, height=-2, width=26)
    return btn

def flash_entry_red(entry):
    """★ إضافة (إصدار 9 — الميزة 5): حقل كلمة المرور يلتون بإطار أحمر قصير
    (~0.9 ثانية) ثم يعود طبيعياً تماماً كما كان — ملفوف بالكامل فلا يخطئ أبداً"""
    try:
        orig = (entry.cget("highlightthickness"), entry.cget("highlightbackground"),
                entry.cget("highlightcolor"))
        entry.config(highlightthickness=2, highlightbackground=RED, highlightcolor=RED)
        def _back():
            try:
                entry.config(highlightthickness=orig[0], highlightbackground=orig[1],
                             highlightcolor=orig[2])
            except Exception:
                pass
        entry.after(900, _back)
    except Exception:
        pass

def shake_widget(widget, seq=(-10, 10, -8, 8, -6, 6, -4, 4, -2, 2, 0), ms=45):
    """★ إضافة (إصدار 9 — الميزة 5): اهتزاز أفقي قصير (~نصف ثانية) للبطاقة
    الوسطية ثم عودتها لمكانها — يعمل فقط على عناصر place (بطاقة الدخول
    توضع بـ place لدعم انزلاق الظهور)، وإلا يُتجاهل بهدوء"""
    if not widget.place_info():
        return
    i = [0]
    def _step():
        try:
            if i[0] >= len(seq):
                widget.place_configure(x=0)
                return
            widget.place_configure(x=seq[i[0]])
            i[0] += 1
            widget.after(ms, _step)
        except Exception:
            pass
    _step()

def fade_in_window(win, card, duration=300, steps=10, slide=26):
    """★ إضافة (إصدار 9 — الميزة 7): ظهور تدريجي — شفافية النافذة ترتفع من
    0 إلى 1.0 خلال ~300 مللي ثانية والبطاقة تنزلق من الأسفل للأعلى قليلاً
    أثناء التلاشي — ولو لم يدعم النظام alpha يُتجاهل بهدوء (try/except)
    وتظهر النافذة فوراً مع بقاء الانزلاق يعمل"""
    alpha_ok = True
    try:
        win.attributes("-alpha", 0.0)
    except Exception:
        alpha_ok = False
    i = [0]
    def _step():
        try:
            i[0] += 1
            t = i[0] / steps
            if alpha_ok:
                try:
                    win.attributes("-alpha", min(t, 1.0))
                except Exception:
                    pass
            if card is not None and card.place_info():
                card.place_configure(y=int(slide * (1 - t)))
            if i[0] < steps:
                win.after(duration // steps, _step)
        except Exception:
            pass
    win.after(duration // steps, _step)

def login_greeting():
    """★ إضافة (إصدار 9 — تصميم النافذة): تحية حسب الوقت (صباح الخير /
    مساء الخير) مع اسم اليوم والتاريخ — بنفس دالة اليوم العربي القائمة"""
    hello = "صباح الخير ☀️" if datetime.now().hour < 12 else "مساء الخير 🌙"
    return f"{hello} — {day_name(today_str())} {today_str()}"

def login_bg_file():
    """★ إضافة (إصدار 9 — الميزة 8): مسار صورة خلفية شاشة الدخول — اسم ثابت
    داخل مجلد البيانات (تُحوَّل png عبر pillow وتُحفظ بهذا الاسم)"""
    return os.path.join(data_dir(), "login_bg.png")

def load_login_bg_photo(w, h):
    """★ إضافة (إصدار 9 — الميزة 8): تحميل صورة الخلفية بمقاس النافذة مع
    طبقة داكنة شفافة فوقها (مزج 0.62 بلون البرنامج الكحلي #0f172a — Tk
    Canvas لا يدعم الشفافية فتُدمج الطبقة داخل الصورة نفسها) حتى تبقى
    الحقول واضحة — وأي فشل (بلا pillow/محذوفة/تالفة) يُتجاهل بهدوء
    ويعيد None فتُرسم الخلفية المتدرجة الافتراضية"""
    if not LOGIN_BG_PIL_OK:
        return None
    try:
        path = get_setting("login_bg")
        if not path or not os.path.exists(path):
            return None
        img = _BGImage.open(path).convert("RGB")
        img = img.resize((w, h), _BGImage.LANCZOS)
        dark = _BGImage.new("RGB", (w, h), (15, 23, 42))     # نفس DARK #0f172a
        img = _BGImage.blend(img, dark, 0.62)
        return _BGImageTk.PhotoImage(img)
    except Exception:
        return None

def draw_login_gradient(cv, w, h):
    """★ إضافة (إصدار 9 — تصميم النافذة): الخلفية المتدرجة الكحلية الداكنة
    الافتراضية — خطوط أفقية بتدرج لوني يدوي من أعلى (أفتح) إلى أسفل (أدكن)
    من عائلة ألوان البرنامج نفسها (#1e293b → #020617)"""
    top, bot = (30, 41, 59), (2, 6, 23)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
        cv.create_line(0, y, w, y, fill="#%02x%02x%02x" % (r, g, b))

def _screen_login_build(win, result):
    """★ إضافة (إصدار 9): بناء شاشة تسجيل الدخول المحسّنة كاملة داخل النافذة
    المعطاة — نافذة Tk عند بدء التشغيل (login_flow) أو Toplevel عند التبديل
    (login_dialog) — بنفس منطق التحقق القائم حرفياً وبنفس أسلوب الكود،
    بالشكل والميزات الثماني الجديدة فقط. ترجع البطاقة الوسطية."""
    win.configure(bg=DARK)
    sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
    win.geometry(f"{LOGIN_W}x{LOGIN_H}+{(sw - LOGIN_W) // 2}+{max((sh - LOGIN_H) // 2 - 40, 0)}")
    win.resizable(False, False)
    try:
        win.overrideredirect(True)     # بلا إطار ويندوز — السحب من الخلفية أدناه
    except Exception:
        pass

    # ---------- الخلفية: صورة المحل بطبقة داكنة، أو التدرج الكحلي الافتراضي ----------
    cv = tk.Canvas(win, width=LOGIN_W, height=LOGIN_H, bg=DARK, highlightthickness=0)
    cv.pack(fill="both", expand=True)
    photo = load_login_bg_photo(LOGIN_W, LOGIN_H)
    if photo is not None:
        cv._login_bg_photo = photo      # الاحتفاظ بمرجع حي للصورة (يمنع محوها)
        cv.create_image(0, 0, image=photo, anchor="nw")
    else:
        draw_login_gradient(cv, LOGIN_W, LOGIN_H)

    # ---------- سحب النافذة من أي مكان على الخلفية + زر ✕ أعلى اليسار ----------
    drag = {"x": 0, "y": 0}
    def _press(e):
        drag["x"], drag["y"] = e.x_root - win.winfo_x(), e.y_root - win.winfo_y()
    def _move(e):
        try:
            win.geometry(f"+{e.x_root - drag['x']}+{e.y_root - drag['y']}")
        except Exception:
            pass
    cv.bind("<Button-1>", _press)
    cv.bind("<B1-Motion>", _move)
    # ✕ يغلق نافذة الدخول — فيعاملها البرنامج كإلغاء الدخول تماماً كما هو قائم
    tk.Button(win, text="✕", command=win.destroy, bg=SIDEBAR, fg=BORDER,
              activebackground=RED, activeforeground="white", font=("Segoe UI", 9, "bold"),
              bd=0, relief="flat", cursor="hand2", takefocus=0).place(x=8, y=8, width=30, height=26)
    # ★ إضافة (إصدار 10 — اللمسة): سطر الإصدار أسفل شاشة الدخول — صغير
    # بلون النص الثانوي، فوق الخلفيتين معاً (التدرج أو صورة المحل الداكنة)
    cv.create_text(LOGIN_W // 2, LOGIN_H - 16, text=f"الإصدار {VERSION}",
                   fill="#94a3b8", font=("Segoe UI", 9))

    # ---------- البطاقة الوسطية: CARD بإطار BORDER أسمك قليلاً (زوايا ظاهرة) ----------
    # توضع بـ place في المنتصف لتدعم الانزلاق عند الظهور والاهتزاز عند الخطأ
    card = tk.Frame(win, bg=CARD, highlightbackground=BORDER, highlightthickness=2)
    card.place(in_=win, relx=0.5, rely=0.5, anchor="c", width=360, y=26)

    def finish(name, role):
        result["name"] = name
        result["role"] = role
        win.destroy()

    def clear_card():
        for w in card.winfo_children():
            w.destroy()

    def field_row(label_text, show=""):
        """صف حقل بنفس نمط صفوف البرنامج القائمة تماماً (تسمية يميناً)"""
        fr = tk.Frame(card, bg=CARD)
        fr.pack(fill="x", padx=26, pady=5)
        tk.Label(fr, text=label_text, bg=CARD, fg=DARK, font=FB,
                 width=18, anchor="e").pack(side="right")
        e = tk.Entry(fr, font=F, justify="center", show=show, relief="solid", bd=1, width=12)
        e.pack(side="right", padx=(0, 8), ipady=4)
        return e

    def err_label():
        """سطر رسالة الخطأ الأحمر داخل البطاقة — يظهر مع الاهتزاز معاً"""
        lbl = tk.Label(card, text="", bg=CARD, fg=RED, font=("Segoe UI", 9, "bold"),
                       wraplength=300, justify="center")
        lbl.pack(fill="x", padx=20, pady=(6, 0))
        return lbl

    # ------------------ شاشة إنشاء حساب المدير (أول تشغيل) ------------------
    def build_create_manager():
        """نفس شاشة إنشاء المدير القائمة بنفس منطقها حرفياً — بالميزات الجديدة:
        زر عين + شريط قوة + منع الضعيفة جداً + اهتزاز البطاقة عند الخطأ"""
        clear_card()
        tk.Label(card, text="👑", bg=CARD, fg=DARK, font=("Segoe UI", 26)).pack(pady=(16, 2))
        tk.Label(card, text="إنشاء حساب المدير (أول تشغيل)",
                 bg=CARD, fg=DARK, font=FT).pack(pady=(0, 8))
        e_user = field_row("اسم المستخدم:")
        e_p1 = field_row("كلمة المرور:", "•")
        add_eye_to_entry(e_p1)                      # ★ (الميزة 1) زر العين داخل الحقل
        e_p2 = field_row("تأكيد كلمة المرور:", "•")
        add_eye_to_entry(e_p2)
        strength_update = make_strength_bar(card)   # ★ (الميزة 4) الشريط تحت الحقل
        e_p1.bind("<KeyRelease>", lambda _e: strength_update(e_p1.get()))
        err_lbl = err_label()
        e_user.focus_set()

        def fail(msg, entry=None):
            """رسالة الخطأ كما هي + اهتزاز البطاقة (كلاهما معاً) — الميزة 5 —
            ومعهما وميض إطار أحمر قصير إن كان الخطأ في حقل كلمة مرور"""
            err_lbl.config(text=msg)
            shake_widget(card)
            if entry is not None:
                flash_entry_red(entry)
            messagebox.showwarning("تنبيه", msg, parent=win)

        def do_create():
            name, p1, p2 = e_user.get().strip(), e_p1.get(), e_p2.get()
            if not name:
                fail("اكتب اسم المستخدم"); return
            # ★ تعديل مصرح به (الميزة 4): الضعيفة جداً (أقل من 5 أحرف = أحمر
            # في شريط القوة) تمنع الحفظ — كانت «4 أحرف على الأقل»
            if pw_is_weak(p1):
                fail("كلمة المرور ضعيفة جداً — استخدم 5 أحرف على الأقل", e_p1); return
            if p1 != p2:
                fail("التأكيد لا يطابق كلمة المرور", e_p1); return
            salt = secrets.token_hex(16)
            with connect() as conn:
                conn.execute("INSERT INTO users(username,password_hash,role,active,created_at) "
                             "VALUES(?,?,?,?,?)",
                             (name, salt + "$" + hash_pwd(salt, p1), "مدير", 1,
                              datetime.now().strftime("%Y-%m-%d %H:%M")))
            CURRENT_USER["name"] = name
            audit("إنشاء حساب مدير", f"أول تشغيل — {name}")
            set_setting("last_user", name)          # ★ (الميزة 3) تذكر آخر مستخدم
            finish(name, "مدير")
        e_p2.bind("<Return>", lambda e: do_create())
        tk.Button(card, text="💾 إنشاء الحساب ودخول", command=do_create, bg=GREEN, fg="white",
                  activebackground=GREEN, activeforeground="white", font=FB, bd=0, cursor="hand2",
                  padx=18, pady=8, highlightthickness=0, width=22).pack(pady=(10, 18))

    # ------------------ شاشة الدخول نفسها ------------------
    def build_login():
        """نفس شاشة الدخول القائمة بنفس منطق التحقق حرفياً (نفس الرسائل الثلاثة
        ونفس تسجيل المحاولات الفاشلة ونفس شرط active=1) بشكلها الجديد"""
        clear_card()
        store = get_setting("store_name") or "نظام المبيعات والمُرتجعات"
        tk.Label(card, text="🏪", bg=CARD, fg=DARK, font=("Segoe UI", 26)).pack(pady=(16, 0))
        tk.Label(card, text=store, bg=CARD, fg=DARK, font=FT).pack()
        tk.Label(card, text=login_greeting(), bg=CARD, fg=GRAY,
                 font=("Segoe UI", 9)).pack(pady=(0, 10))
        # اسم المستخدم: نفس القائمة المنسدلة القائمة (المدير أولاً ثم أبجدياً)
        fr_user = tk.Frame(card, bg=CARD)
        fr_user.pack(fill="x", padx=26, pady=5)
        tk.Label(fr_user, text="اسم المستخدم:", bg=CARD, fg=DARK, font=FB,
                 width=18, anchor="e").pack(side="right")
        users = active_users_list()
        e_user = ttk.Combobox(fr_user, font=F, width=12, justify="center", values=users)
        e_user.pack(side="right", padx=(0, 8), ipady=4)
        # ★ (الميزة 3) تذكر آخر مستخدم: المحفوظ هو المختار افتراضياً، وإن غاب
        # (موقوف/محذوف) فالمدير أولاً كما هو — والمؤشر جاهز في كلمة المرور
        last = get_setting("last_user") or ""
        if last and last in users:
            e_user.set(last)
        elif users:
            e_user.current(0)
        e_pwd = field_row("كلمة المرور:", "•")
        add_eye_to_entry(e_pwd)                     # ★ (الميزة 1) زر العين داخل الحقل
        err_lbl = err_label()

        # ★ (الميزة 2) زر الدخول العريض بعرض البطاقة بلون ACCENT: أفتح عند مرور
        # المؤشر، أغمق لحظة الضغط 150 مللي ثم يعود — ويتوقف كلياً في «جارٍ التحقق»
        HOVER, PRESSED = "#3b82f6", "#1d4ed8"
        verifying = {"on": False}                   # ★ (الميزة 6) منع الضغط المزدوج
        hover_on = {"v": False}
        btn = tk.Button(card, text="دخول", command=lambda: try_login(),
                        bg=ACCENT, fg="white", activebackground=HOVER, activeforeground="white",
                        disabledforeground="white", font=FB, bd=0, cursor="hand2",
                        padx=18, pady=10, highlightthickness=0, takefocus=0)
        btn.pack(fill="x", padx=26, ipady=2, pady=(10, 4))

        def _enter(_e):
            hover_on["v"] = True
            if not verifying["on"]:
                btn.config(bg=HOVER)
        def _leave(_e):
            hover_on["v"] = False
            if not verifying["on"]:
                btn.config(bg=ACCENT)
        def _press_fx(_e):
            if not verifying["on"]:
                btn.config(bg=PRESSED)
                btn.after(150, lambda: btn.config(
                    bg=PRESSED if verifying["on"] else (HOVER if hover_on["v"] else ACCENT)))
        btn.bind("<Enter>", _enter)
        btn.bind("<Leave>", _leave)
        btn.bind("<Button-1>", _press_fx)

        def fail_login(msg, clear_pwd=False):
            """عند الخطأ: الزر يعود لنصه وحالته + اهتزاز البطاقة نصف ثانية +
            وميض إطار أحمر قصير للحقل — ورسالة الخطأ النصية تبقى معهما (الميزة 5)"""
            verifying["on"] = False
            btn.config(text="دخول", state="normal", bg=ACCENT, cursor="hand2")
            err_lbl.config(text=msg)
            shake_widget(card)
            flash_entry_red(e_pwd)
            messagebox.showerror("خطأ", msg, parent=win)
            try:
                if clear_pwd:
                    e_pwd.delete(0, "end")
                e_pwd.focus_set()
                e_pwd.select_range(0, "end")
            except Exception:
                pass

        def try_login(_e=None):
            if verifying["on"]:
                return               # ★ (الميزة 6) منع الضغط المزدوج أثناء التحقق
            name, pwd = e_user.get().strip(), e_pwd.get()
            if not name:
                err_lbl.config(text="اكتب اسم المستخدم")
                shake_widget(card)
                messagebox.showerror("خطأ", "اكتب اسم المستخدم", parent=win); return
            # ★ (الميزة 6) حالة «جارٍ التحقق...»: الزر يتعطل وينتظر 400 مللي
            # قبل عرض النتيجة بإحساس طبيعي — والدخول الناجح يكمل فوراً بعدها
            verifying["on"] = True
            btn.config(text="جارٍ التحقق...", state="disabled", bg=PRESSED, cursor="watch")

            def do_verify():
                row = get_user_row(name)
                if row is None:
                    CURRENT_USER["name"] = name   # المحاولة الفاشلة تُسجل باسم المُجرّب
                    audit("محاولة دخول فاشلة", f"اسم المستخدم غير موجود: {name}")
                    fail_login("اسم المستخدم غير موجود")
                elif not verify_user_password(row, pwd):
                    CURRENT_USER["name"] = name
                    audit("محاولة دخول فاشلة", f"كلمة المرور خاطئة: {name}")
                    fail_login("كلمة المرور خاطئة", clear_pwd=True)
                elif not row["active"]:
                    CURRENT_USER["name"] = name
                    audit("محاولة دخول فاشلة", f"حساب موقوف: {name}")
                    fail_login("هذا الحساب موقوف — راجع المدير")
                else:
                    set_setting("last_user", row["username"])   # ★ (الميزة 3) تذكر آخر مستخدم
                    CURRENT_USER["name"] = row["username"]
                    audit("تسجيل دخول", f"{row['username']} ({row['role']})")
                    finish(row["username"], row["role"])
            win.after(400, do_verify)
        e_pwd.bind("<Return>", try_login)
        e_user.bind("<Return>", lambda e: e_pwd.focus_set())
        tk.Label(card, text="🔒 تُسجَّل كل محاولات الدخول في سجل التدقيق",
                 bg=CARD, fg=GRAY, font=("Segoe UI", 8)).pack(pady=(2, 16))
        # المؤشر جاهز في كلمة المرور بعد اكتمال الظهور التدريجي (الميزتان 3+7)
        win.after(380, lambda: (e_pwd if e_user.get() else e_user).focus_set())

    if users_count() == 0:
        build_create_manager()      # نفس سلوك أول تشغيل القائم تماماً
    else:
        build_login()
    fade_in_window(win, card)       # ★ (الميزة 7) تلاشي + انزلاق البطاقة
    return card


def login_flow():
    """★ (إصدار 3 — ميزة 2) تسجيل الدخول بحساب مستخدم —
    ترجع {"name": اسم المستخدم, "role": "مدير"/"بائع"} أو None عند الإغلاق بدون دخول.
    أول تشغيل (جدول users فارغ): شاشة إنشاء حساب المدير.
    الدخول القديم «دخول كبائع» استُبدل بالحسابات.
    ★ تعديل مصرح به (إصدار 9): إعادة بناء كود بناء النافذة بالشكل والميزات
    الثماني الجديدة — بنفس منطق التحقق الحالي تماماً (التعديل المصرح به الوحيد)"""
    init_db()
    ensure_users_upgraded()   # ★ ترقية تلقائية: كلمة مرور المدير القديمة تتحول لحساب «مدير»
    win = tk.Tk()
    result = {"name": None, "role": None}
    _screen_login_build(win, result)
    win.protocol("WM_DELETE_WINDOW", win.destroy)
    win.mainloop()
    return result if result["role"] else None


if __name__ == "__main__":
    try:
        creds = login_flow()             # ★ تعديل ضروري معلن (إصدار 3): بوابة الدخول بالحسابات
        if creds is None:
            sys.exit(0)                  # أُغلقت نافذة الدخول بدون تسجيل دخول
        # ★ تعديل ضروري معلن (إصدار 3 — ميزة 2): تمرير اسم المستخدم ودوره بعد الدخول
        # ★ تعديل ضروري معلن (إصدار 10 — نظام التحديث): نفس إنشاء التطبيق
        # وتشغيله السابق تماماً، مع تفكيكه لسطرين كي يبدأ الفحص التلقائي
        # الصامت للتحديث بعد الدخول مباشرة (after 1500) — لا يبطئ الفتح
        # ولا يظهر شيئاً أثناءه، وأي فشل صمت تام
        app = App(role=creds["role"], user_name=creds["name"])
        app.after(1500, lambda: update_check_silent(app))
        app.mainloop()
    except Exception as e:
        # ★ تعذر فتح البرنامج: صندوق عربي واضح بدل نافذة تُغلق بصمت
        log_error(e, sys.exc_info()[2])
        print(traceback.format_exc(), file=sys.stderr)
        try:
            root = tk._default_root or tk.Tk()
            root.withdraw()
            messagebox.showerror("تعذر تشغيل البرنامج",
                "حدث خطأ منع فتح البرنامج:\n\n"
                f"{type(e).__name__}: {e}\n\n"
                "سُجل الخطأ في error_log.txt.\n"
                f"مجلد البيانات: {os.path.dirname(DB)}\n\n"
                "− أغلق أي نسخة أخرى مفتوحة من البرنامج ثم أعد المحاولة.\n"
                "− شغّل البرنامج من مجلد عادي (ليس من داخل ملف ZIP ولا مجلداً محمياً مثل Program Files).")
            root.destroy()
        except Exception:
            pass
        sys.exit(1)
