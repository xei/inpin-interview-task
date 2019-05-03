package com.xei.inpin

import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class EditAgencyActivity : AppCompatActivity() {

    private lateinit var nameEditText: EditText
    private lateinit var parentIdEditText: EditText
    private lateinit var updateButton: Button

    companion object {
        fun start(context: Context, id: Int, name: String, parentId: Int) {
            val intent = Intent(context, EditAgencyActivity::class.java)
            intent.putExtra("id", id)
            intent.putExtra("name", name)
            intent.putExtra("parent_id", parentId)
            context.startActivity(intent)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_edit_agency)

        nameEditText = findViewById(R.id.editText_name)
        nameEditText.setText(intent.getStringExtra("name"))
        parentIdEditText = findViewById(R.id.editText_parentId)
        parentIdEditText.setText(intent.getIntExtra("parent_id", 0).toString())

        updateButton = findViewById(R.id.button_update)
        updateButton.setOnClickListener {
            val webApi = RetrofitHelper.getRetrofit(null).create(AgencyWebApi::class.java)
            val call = webApi.updateAgency(
                intent.getIntExtra("id", 0),
                nameEditText.text.toString(),
                parentIdEditText.text.toString().toInt()
            )
            call.enqueue(object : Callback<Message> {
                override fun onFailure(call: Call<Message>, t: Throwable) {}

                override fun onResponse(call: Call<Message>, response: Response<Message>) {
                    Toast.makeText(this@EditAgencyActivity, response.body()?.msg, Toast.LENGTH_LONG).show()
                    finish()
                }
            })
        }
    }
}
