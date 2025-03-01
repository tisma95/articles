import 'package:flutter_translation_app/locales/en.dart';
import 'package:flutter_translation_app/locales/fr.dart';

class AppLocalization {
  AppLocalization({required this.lang});

  String lang = "en";

  static final _localizedValues = <String, Map<String, String>>{
    'en': EnLang().locales,
    'fr': FrLang().locales,
  };

  static List<String> languages() => _localizedValues.keys.toList();

  String translation(key) {
    return _localizedValues[lang]![key] ?? key;
  }
}
