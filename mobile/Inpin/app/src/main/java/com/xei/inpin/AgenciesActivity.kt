package com.xei.inpin

import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.widget.Button
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.Retrofit




class AgenciesActivity : AppCompatActivity() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var addButton: Button

    private val myDataset = ArrayList<Agency>()

    companion object {
        fun start(context: Context) {
            context.startActivity(Intent(context, AgenciesActivity::class.java))
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_agencies)


        recyclerView = findViewById<RecyclerView>(R.id.agencies_recycler_view).apply {
            setHasFixedSize(true)
            layoutManager = LinearLayoutManager(this@AgenciesActivity)
            adapter = AgenciesViewAdapter(myDataset)
        }

        findViewById<Button>(R.id.button_addAgency).setOnClickListener {
            NewAgencyActivity.start(this@AgenciesActivity)
        }

    }

    override fun onResume() {
        super.onResume()
        val webApi = RetrofitHelper.getRetrofit(null).create(AgencyWebApi::class.java)
        val call = webApi.listAgencies()
        call.enqueue(object: Callback<List<Agency>>{
            override fun onFailure(call: Call<List<Agency>>, t: Throwable) {}

            override fun onResponse(call: Call<List<Agency>>, response: Response<List<Agency>>) {
                myDataset.clear()
                myDataset.addAll(response.body()!!)
                recyclerView.adapter?.notifyDataSetChanged()
            }
        })
    }
}