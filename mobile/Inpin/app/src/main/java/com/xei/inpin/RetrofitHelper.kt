package com.xei.inpin

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class RetrofitHelper {

    companion object {
        private var retrofit: Retrofit? = null
        fun getRetrofit(baseUrl: String?) : Retrofit{
            if(retrofit != null) {
                return retrofit as Retrofit
            } else {
                retrofit = Retrofit.Builder()
                    .baseUrl(baseUrl) // "http://192.168.43.16:5000"
                    .addConverterFactory(GsonConverterFactory.create())
                    .build()
                return retrofit as Retrofit
            }
        }
    }

}