package com.xei.inpin

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import android.widget.Toast
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class AgenciesViewAdapter(private val mDataset: ArrayList<Agency>) :
    RecyclerView.Adapter<AgenciesViewAdapter.AgenciesItemViewHolder>() {

    override fun getItemCount() = mDataset.size

    override fun onCreateViewHolder(parent: ViewGroup, position: Int): AgenciesItemViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.row_list_agencies, parent, false)
        return AgenciesItemViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: AgenciesItemViewHolder, position: Int) {
        holder.nameTextView.text = mDataset[position].name
        holder.deleteButton.setOnClickListener {
            val webApi = RetrofitHelper.getRetrofit(null).create(AgencyWebApi::class.java)
            val call = webApi.deleteAgency(mDataset[position].id)
            call.enqueue(object : Callback<Message> {
                override fun onFailure(call: Call<Message>, t: Throwable) {}

                override fun onResponse(call: Call<Message>, response: Response<Message>) {
                    Toast.makeText(holder.itemView.context, response.body()?.msg, Toast.LENGTH_LONG).show()
                    mDataset.removeAt(position)
                    notifyDataSetChanged()
                }
            })
        }
        holder.editButton.setOnClickListener {
            EditAgencyActivity.start(
                holder.itemView.context,
                mDataset[position].id, mDataset[position].name, mDataset[position].parentId
            )
        }
        holder.itemView.setOnClickListener {
            AgencyDetailsActivity.start(
                holder.itemView.context,
                mDataset[position].id, mDataset[position].name, mDataset[position].parentId
            )
        }
    }

    class AgenciesItemViewHolder(rootView: View) : RecyclerView.ViewHolder(rootView) {
        val nameTextView = rootView.findViewById<TextView>(R.id.textView_name)!!
        val deleteButton = rootView.findViewById<View>(R.id.imageView_delete)!!
        val editButton = rootView.findViewById<View>(R.id.imageView_edit)!!
    }
}