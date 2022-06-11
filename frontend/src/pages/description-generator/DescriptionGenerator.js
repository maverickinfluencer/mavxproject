import React, { useEffect, useState } from 'react'
import axios from 'axios'
import './description-generator.css'
import { AiOutlinePlusCircle } from 'react-icons/ai';
import qs from 'qs'
import DOMPurify from "dompurify";

const DescriptionGenerator = () => {
    const [brandName, setBrandName] = useState("")
    const [brandInfo, setBrandInfo] = useState([])
    const [links, setLinks] = useState([{}])
    const [couponCode, setCouponCode] = useState("")
    const [influencerName, setInfluencerName] = useState("")
    console.log(links);
    const [priceInfo, setPriceInfo] = useState();
    useEffect(() => {
        console.log("useEffect called.");
        axios.get("http://127.0.0.1:5000/api/v1/admin/video-description/brand-info/" + brandName).then((res) => {
            console.log(res.data);
            setBrandInfo(res.data)
        })
    }, [brandName])
    const handleLinkAdd = () => {
        setLinks([...links, {}])
    }
    const handleLinkRemove = (index) => {
        const list = [...links];
        list.splice(index, 1);
        setLinks(list);
    }
    const handleLinkChange = (e, index) => {
        const { name, value } = e.target;
        const list = [...links]
        list[index][name] = value;
        setLinks(list);
    }
    const handlePriceInfo = (e) => {
        e.preventDefault();
        axios({
            method: 'post',
            url: 'http://65.0.7.27:5000/api/v1/admin/price-info',
            data: JSON.stringify({
                brand_name: brandName,
                influencer_name: influencerName,
                coupon_code: couponCode,
                product_links: links,
                discount: brandInfo[2]

            }),
            headers: {
                'content-type': 'application/json'
            }
        }).then((res) => {
            console.log(res.data);
            setPriceInfo(res.data)
        })
    }
    const mySafeHTML = DOMPurify.sanitize(priceInfo);
    return (
        <div className="container" >
            <div className="container-wrapper">
                <div class="card" style={{ width: "100%" }}>
                    <div className="card-header">
                        Description Generator
                    </div>
                    <div className="card-body">
                        <div className="dropdown">
                            <button className="btn btn-info dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Select Brand
                            </button>
                            <div className="dropdown-menu" aria-labelledby="dropdownMenu2">
                                <button className="dropdown-item" type="button" onClick={(e) => { setBrandName("Fashor") }} >Fashor</button>
                                <button className="dropdown-item" type="button" onClick={(e) => { setBrandName("Indya") }} >Indya</button>
                                <button className="dropdown-item" type="button" onClick={(e) => { setBrandName("Rustorange") }} >Rustorange</button>
                                <button className="dropdown-item" type="button" onClick={(e) => { setBrandName("Juniper") }} >Juniper</button>
                            </div>
                        </div>
                        <div className="card text-center">
                            <div className="card-header">
                                {brandName}
                            </div>
                            <div className="card-body">
                                <h5 className="card-title">Brand Url : {brandInfo[1]}</h5>
                                <h5 className="card-title">Discount percent : {brandInfo[2]} %</h5>
                                <p className="card-text">tags: <span style={{ color: 'blue' }} >{brandInfo[3]}</span> </p>
                            </div>
                        </div>
                        <div class="row g-3 align-items-center mt-5">
                            <div class="col-auto">
                                <label for="influencer-name" class="col-form-label">Influencer Name</label>
                            </div>
                            <div class="col-auto">
                                <input
                                    name="influencerName"
                                    value={influencerName}
                                    onChange={(e) => setInfluencerName(e.target.value)}
                                    type="text" id="influencer-name" class="form-control" aria-describedby="passwordHelpInline" required />
                            </div>
                            <div class="col-auto">
                                <label for="coupon-code" class="col-form-label">Coupon Code</label>
                            </div>
                            <div class="col-auto">
                                <input
                                    name="couponCode"
                                    value={couponCode}
                                    onChange={(e) => setCouponCode(e.target.value)}
                                    type="text" id="coupon-code" class="form-control" aria-describedby="passwordHelpInline" required />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-sm-12">
                                <h5 className="mt-3 mb-4 fw-bold" >Links</h5>
                                {links.map((singleLink, index) => (
                                    <div key={index} className="row mb-3">
                                        <div className="form-group col-md-8">
                                            <input
                                                name="link"
                                                value={singleLink.link}
                                                onChange={(e) => handleLinkChange(e, index)}
                                                type="text" className="form-control" placeholder="Enter link" required />
                                        </div>
                                        {links.length > 1 &&
                                            <div className="form-group col-md-2">
                                                <button onClick={handleLinkRemove} className="btn btn-danger">Remove</button>
                                            </div>
                                        }

                                        {links.length - 1 === index &&
                                            <div className="form-group col-md-2">
                                                <button onClick={handleLinkAdd} className="btn btn-primary">Add more</button>
                                            </div>}
                                    </div>
                                ))}
                            </div>

                            {/* <AiOutlinePlusCircle onClick={handleLinkAdd}   color='blue' size={30} /> */}
                        </div>
                        <div className="row">
                            <div className="col-sm-12">
                                <div className="row mb-3" >
                                    <div className="form-group col-md-6">
                                        <button onClick={handlePriceInfo} className="btn btn-info">Generate Price Info</button>
                                    </div>
                                    <div className="form-group col-md-6">
                                        <button onClick={handlePriceInfo} className="btn btn-info">Generate Description</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="row" >
                            <div className="col-sm-12">
                                <div className="row mb-3" >
                                    <div className="form-group col-md-6">
                                        <div className="card" style={{ width:"100%"}} >
                                            <div className="card-body">
                                            <div dangerouslySetInnerHTML={{ __html: mySafeHTML }} />
                                            
                                            </div>
                                        </div>
                                    </div>
                                    <div className="form-group col-md-6">
                                        <div className="card" style={{ width:"100%"}}>
                                            <div className="card-body">
                                                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor, blanditiis iusto. Magni odio distinctio fuga natus iusto. Praesentium, soluta eius, iure molestias officiis maxime a animi eveniet maiores sapiente porro.
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DescriptionGenerator