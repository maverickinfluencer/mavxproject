(this.webpackJsonpmyrouter=this.webpackJsonpmyrouter||[]).push([[0],{101:function(e,t,c){},102:function(e,t,c){},109:function(e,t,c){},130:function(e,t,c){},141:function(e,t){},144:function(e,t,c){"use strict";c.r(t);var n=c(0),a=c(29),s=c.n(a),i=(c(101),c(102),c(7)),r=c(206),o=c(209),l=c(207),d=c(210),j=c(208),b=c(201),u=c(84),m=c.n(u),h=c(204),x=c(205),O=c(200),p=c(203),f=c(10),v=c(35),N=c(1),g=["Profile","Account","Dashboard","Logout"],y=function(){var e=Object(f.f)(),t=n.useState(null),c=Object(i.a)(t,2),a=c[0],s=c[1],u=n.useState(null),y=Object(i.a)(u,2),w=y[0],k=y[1],C=function(){k(null)},D=function(t){t.preventDefault(),e("/admin")};return Object(N.jsx)(r.a,{position:"static",children:Object(N.jsx)(h.a,{maxWidth:"xl",children:Object(N.jsxs)(l.a,{disableGutters:!0,children:[Object(N.jsx)(v.b,{to:"/",className:"link",children:Object(N.jsx)(j.a,{variant:"h6",noWrap:!0,component:"div",sx:{color:"white",mr:2,display:{xs:"none",md:"flex"}},children:"MavX.io"})}),Object(N.jsxs)(o.a,{sx:{flexGrow:1,display:{xs:"flex",md:"none"}},children:[Object(N.jsx)(d.a,{size:"large","aria-label":"account of current user","aria-controls":"menu-appbar","aria-haspopup":"true",onClick:function(e){s(e.currentTarget)},color:"inherit",children:Object(N.jsx)(m.a,{})}),Object(N.jsxs)(b.a,{id:"menu-appbar",anchorEl:a,anchorOrigin:{vertical:"bottom",horizontal:"left"},keepMounted:!0,transformOrigin:{vertical:"top",horizontal:"left"},open:Boolean(a),onClose:function(){s(null)},sx:{display:{xs:"block",md:"none"}},children:[Object(N.jsx)(p.a,{onClick:D,children:Object(N.jsx)(j.a,{textAlign:"center",children:"Admin"})}),Object(N.jsx)(p.a,{onClick:"#",children:Object(N.jsx)(j.a,{textAlign:"center",children:"User"})})]})]}),Object(N.jsx)(j.a,{variant:"h6",noWrap:!0,component:"div",sx:{flexGrow:1,display:{xs:"flex",md:"none"}},children:Object(N.jsx)(v.b,{to:"/",className:"link",children:"Mavx.io"})}),Object(N.jsxs)(o.a,{sx:{flexGrow:1,display:{xs:"none",md:"flex"}},children:[Object(N.jsx)(x.a,{onClick:D,sx:{my:2,color:"white",display:"block"},children:"Admin"}),Object(N.jsx)(x.a,{onClick:"#",sx:{my:2,color:"white",display:"block"},children:"User"})]}),Object(N.jsxs)(o.a,{sx:{flexGrow:0},children:[Object(N.jsx)(O.a,{title:"Login",children:Object(N.jsx)(d.a,{sx:{p:0},children:Object(N.jsx)(j.a,{variant:"h6",noWrap:!0,component:"div",sx:{my:2,color:"white",flexGrow:1,display:{xs:"flex",md:"flex"}},children:"Login"})})}),Object(N.jsx)(b.a,{sx:{mt:"45px"},id:"menu-appbar",anchorEl:w,anchorOrigin:{vertical:"top",horizontal:"right"},keepMounted:!0,transformOrigin:{vertical:"top",horizontal:"right"},open:Boolean(w),onClose:C,children:g.map((function(e){return Object(N.jsx)(p.a,{onClick:C,children:Object(N.jsx)(j.a,{textAlign:"center",children:e})},e)}))})]})]})})})},w=(c(109),c(44)),k=c.n(w);var C=function(){var e=Object(n.useState)({}),t=Object(i.a)(e,2),c=t[0],a=t[1];return Object(n.useEffect)((function(){k.a.get("http://65.0.7.27:5000/api/v1/admin/video-data/status").then((function(e){console.log(e.data),a(e.data)}))}),[]),console.log(c),Object(N.jsx)("div",{className:"wrapper",children:Object(N.jsxs)("div",{className:"card",children:[Object(N.jsx)("div",{className:"card-header",children:"Video Data V1"}),Object(N.jsxs)("div",{className:"card-body",children:[Object(N.jsxs)("h4",{className:"card-title",children:["Last run :",c.last_run]}),Object(N.jsxs)("h4",{className:"card-text",children:["Status : ",c.video_data_status," "]}),Object(N.jsxs)("div",{className:"btns",children:[Object(N.jsx)("button",{onClick:function(){window.open("https://docs.google.com/spreadsheets/d/1pCI31UUBQtMJiH2mAqjeC3siE0Pks3yu1xRupS8a9QY/edit#gid=0")},className:"btn btn-primary",children:"Today Data"}),Object(N.jsx)("button",{onClick:function(){window.open("https://docs.google.com/spreadsheets/d/1hq-i4YKAGv7HvirtjqL-8TNOH0RPHXUTqyFy8oOLSFE/edit#gid=0")},className:"btn btn-primary",children:"Historical Data"})]})]})]})})},D=function(){var e=Object(f.f)();return Object(N.jsx)(N.Fragment,{children:Object(N.jsx)("div",{className:"wrapper",children:Object(N.jsxs)("div",{className:"card",children:[Object(N.jsx)("div",{className:"card-header",children:"Video Data V1"}),Object(N.jsx)("div",{className:"card-body",children:Object(N.jsxs)("div",{className:"btns",children:[Object(N.jsx)("button",{onClick:function(t){t.preventDefault(),e("/admin/video-data")},className:"btn btn-primary",children:"Video Data"}),Object(N.jsx)("button",{onClick:function(t){t.preventDefault(),e("/admin/description-generator")},className:"btn btn-primary",children:"Description Generator Data"})]})})]})})})};c(128),c(129);var S=function(){return Object(N.jsx)("div",{children:Object(N.jsx)("h1",{children:"Home Page"})})},G=c(16),A=(c(130),c(131),c(85)),E=c.n(A),H=function(){var e=Object(n.useState)(""),t=Object(i.a)(e,2),c=t[0],a=t[1],s=Object(n.useState)([]),r=Object(i.a)(s,2),o=r[0],l=r[1],d=Object(n.useState)([{}]),j=Object(i.a)(d,2),b=j[0],u=j[1],m=Object(n.useState)(""),h=Object(i.a)(m,2),x=h[0],O=h[1],p=Object(n.useState)(""),f=Object(i.a)(p,2),v=f[0],g=f[1];console.log(b);var y=Object(n.useState)(),w=Object(i.a)(y,2),C=w[0],D=w[1];Object(n.useEffect)((function(){console.log("useEffect called."),k.a.get("http://65.0.7.27:5000/api/v1/admin/video-description/brand-info/"+c).then((function(e){console.log(e.data),l(e.data)}))}),[c]);var S=function(){u([].concat(Object(G.a)(b),[{}]))},A=function(e){var t=Object(G.a)(b);t.splice(e,1),u(t)},H=function(e){e.preventDefault(),k()({method:"post",url:"http://65.0.7.27:5000/api/v1/admin/price-info",data:JSON.stringify({brand_name:c,influencer_name:v,coupon_code:x,product_links:b,discount:o[2]}),headers:{"content-type":"application/json"}}).then((function(e){console.log(e.data),D(e.data)}))},I=E.a.sanitize(C);return Object(N.jsx)("div",{className:"container",children:Object(N.jsx)("div",{className:"container-wrapper",children:Object(N.jsxs)("div",{class:"card",style:{width:"100%"},children:[Object(N.jsx)("div",{className:"card-header",children:"Description Generator"}),Object(N.jsxs)("div",{className:"card-body",children:[Object(N.jsxs)("div",{className:"dropdown",children:[Object(N.jsx)("button",{className:"btn btn-info dropdown-toggle",type:"button",id:"dropdownMenu2","data-toggle":"dropdown","aria-haspopup":"true","aria-expanded":"false",children:"Select Brand"}),Object(N.jsxs)("div",{className:"dropdown-menu","aria-labelledby":"dropdownMenu2",children:[Object(N.jsx)("button",{className:"dropdown-item",type:"button",onClick:function(e){a("Fashor")},children:"Fashor"}),Object(N.jsx)("button",{className:"dropdown-item",type:"button",onClick:function(e){a("Indya")},children:"Indya"}),Object(N.jsx)("button",{className:"dropdown-item",type:"button",onClick:function(e){a("Rustorange")},children:"Rustorange"}),Object(N.jsx)("button",{className:"dropdown-item",type:"button",onClick:function(e){a("Juniper")},children:"Juniper"})]})]}),Object(N.jsxs)("div",{className:"card text-center",children:[Object(N.jsx)("div",{className:"card-header",children:c}),Object(N.jsxs)("div",{className:"card-body",children:[Object(N.jsxs)("h5",{className:"card-title",children:["Brand Url : ",o[1]]}),Object(N.jsxs)("h5",{className:"card-title",children:["Discount percent : ",o[2]," %"]}),Object(N.jsxs)("p",{className:"card-text",children:["tags: ",Object(N.jsx)("span",{style:{color:"blue"},children:o[3]})," "]})]})]}),Object(N.jsxs)("div",{class:"row g-3 align-items-center mt-5",children:[Object(N.jsx)("div",{class:"col-auto",children:Object(N.jsx)("label",{for:"influencer-name",class:"col-form-label",children:"Influencer Name"})}),Object(N.jsx)("div",{class:"col-auto",children:Object(N.jsx)("input",{name:"influencerName",value:v,onChange:function(e){return g(e.target.value)},type:"text",id:"influencer-name",class:"form-control","aria-describedby":"passwordHelpInline",required:!0})}),Object(N.jsx)("div",{class:"col-auto",children:Object(N.jsx)("label",{for:"coupon-code",class:"col-form-label",children:"Coupon Code"})}),Object(N.jsx)("div",{class:"col-auto",children:Object(N.jsx)("input",{name:"couponCode",value:x,onChange:function(e){return O(e.target.value)},type:"text",id:"coupon-code",class:"form-control","aria-describedby":"passwordHelpInline",required:!0})})]}),Object(N.jsx)("div",{className:"row",children:Object(N.jsxs)("div",{className:"col-sm-12",children:[Object(N.jsx)("h5",{className:"mt-3 mb-4 fw-bold",children:"Links"}),b.map((function(e,t){return Object(N.jsxs)("div",{className:"row mb-3",children:[Object(N.jsx)("div",{className:"form-group col-md-8",children:Object(N.jsx)("input",{name:"link",value:e.link,onChange:function(e){return function(e,t){var c=e.target,n=c.name,a=c.value,s=Object(G.a)(b);s[t][n]=a,u(s)}(e,t)},type:"text",className:"form-control",placeholder:"Enter link",required:!0})}),b.length>1&&Object(N.jsx)("div",{className:"form-group col-md-2",children:Object(N.jsx)("button",{onClick:A,className:"btn btn-danger",children:"Remove"})}),b.length-1===t&&Object(N.jsx)("div",{className:"form-group col-md-2",children:Object(N.jsx)("button",{onClick:S,className:"btn btn-primary",children:"Add more"})})]},t)}))]})}),Object(N.jsx)("div",{className:"row",children:Object(N.jsx)("div",{className:"col-sm-12",children:Object(N.jsxs)("div",{className:"row mb-3",children:[Object(N.jsx)("div",{className:"form-group col-md-6",children:Object(N.jsx)("button",{onClick:H,className:"btn btn-info",children:"Generate Price Info"})}),Object(N.jsx)("div",{className:"form-group col-md-6",children:Object(N.jsx)("button",{onClick:H,className:"btn btn-info",children:"Generate Description"})})]})})}),Object(N.jsx)("div",{className:"row",children:Object(N.jsx)("div",{className:"col-sm-12",children:Object(N.jsxs)("div",{className:"row mb-3",children:[Object(N.jsx)("div",{className:"form-group col-md-6",children:Object(N.jsx)("div",{className:"card",style:{width:"100%"},children:Object(N.jsx)("div",{className:"card-body",children:Object(N.jsx)("div",{dangerouslySetInnerHTML:{__html:I}})})})}),Object(N.jsx)("div",{className:"form-group col-md-6",children:Object(N.jsx)("div",{className:"card",style:{width:"100%"},children:Object(N.jsx)("div",{className:"card-body",children:"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolor, blanditiis iusto. Magni odio distinctio fuga natus iusto. Praesentium, soluta eius, iure molestias officiis maxime a animi eveniet maiores sapiente porro."})})})]})})})]})]})})})};var I=function(){return Object(N.jsxs)(v.a,{children:[Object(N.jsx)(y,{}),Object(N.jsxs)(f.c,{children:[Object(N.jsx)(f.a,{exact:!0,path:"/",element:Object(N.jsx)(S,{})}),Object(N.jsx)(f.a,{exact:!0,path:"/admin",element:Object(N.jsx)(D,{})}),Object(N.jsx)(f.a,{exact:!0,path:"/admin/video-data",element:Object(N.jsx)(C,{})}),Object(N.jsx)(f.a,{exact:!0,path:"/admin/description-generator",element:Object(N.jsx)(H,{})})]})]})};s.a.render(Object(N.jsx)(I,{}),document.getElementById("root"))}},[[144,1,2]]]);
//# sourceMappingURL=main.e7f1ce51.chunk.js.map