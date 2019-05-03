package com.xei.inpin

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

class LaunchActivity : AppCompatActivity() {

    private lateinit var baseUrlEditText: EditText
    private lateinit var enterButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_launch)

        baseUrlEditText = findViewById(R.id.editText_baseUrl)
        enterButton = findViewById(R.id.button_enter)
        enterButton.setOnClickListener {
            RetrofitHelper.getRetrofit(baseUrlEditText.text.toString())
            AgenciesActivity.start(this)
            finish()
        }

    }
}
