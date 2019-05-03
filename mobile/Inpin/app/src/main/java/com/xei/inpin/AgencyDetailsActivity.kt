package com.xei.inpin

import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle

class AgencyDetailsActivity : AppCompatActivity() {

    companion object {
        fun start(context: Context, id:Int, name: String, parentId:Int) {
            val intent = Intent(context, AgencyDetailsActivity::class.java)
            intent.putExtra("id", id)
            intent.putExtra("name", name)
            intent.putExtra("parent_id", parentId)
            context.startActivity(intent)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_agency_details)
    }
}
