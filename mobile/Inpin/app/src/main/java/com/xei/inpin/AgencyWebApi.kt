package com.xei.inpin

import retrofit2.Call
import retrofit2.http.*


interface AgencyWebApi {

    @FormUrlEncoded
    @POST("agency")
    fun addAgency(@Field("name") name: String, @Field("parent_id") parentId: Int): Call<Message>

    @GET("agency")
    fun listAgencies(): Call<List<Agency>>

    @FormUrlEncoded
    @PUT("agency/{id}")
    fun updateAgency(@Path("id") id: Int, @Field("name") name: String, @Field("parent_id") parentId: Int): Call<Message>

    @DELETE("agency/{id}")
    fun deleteAgency(@Path("id") id: Int): Call<Message>
}