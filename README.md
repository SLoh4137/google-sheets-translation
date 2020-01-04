# google-sheets-translation
Translating strings in a Google Sheet document into another language. Outputs to the same Google Sheet

Uses the Google Sheet API and the Google Cloud Translation APIs

I realized halfway that you can just use the [`=GOOGLETRANSLATE`](https://jakemiller.net/translate-in-google-sheets/) formula in Google Sheets to achieve the same thing ```¯\_(ツ)_/¯```


[Reading & Writing Cell Values](https://developers.google.com/sheets/api/guides/values)

[Google Cloud Quickstart](https://cloud.google.com/translate/docs/basic/setup-basic) includes information on how to get credentials

[Translating text basic version](https://cloud.google.com/translate/docs/basic/translating-text#translating_text)

A more sophisticated version of this app would be training the Cloud Translation model using phrases if you have a specialized translation dictionary.