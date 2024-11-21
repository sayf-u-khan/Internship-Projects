import "./ImagePage.css";

const ImagePage = () => {
    return (
        <div>
            <img src="/images/image1.jpg" alt="Jade rabbit"></img>
            <h1>Image Things</h1>
            <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, 
            nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula 
            venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa. 
            Fusce luctus vestibulum augue ut aliquet. Mauris ante ligula, facilisis sed ornare eu, 
            lobortis in odio. Praesent convallis urna a lacus interdum ut hendrerit risus congue. 
            Nunc sagittis dictum nisi, sed ullamcorper ipsum dignissim ac. In at libero sed 
            nunc venenatis imperdiet sed ornare turpis. Donec vitae dui eget tellus gravida 
            venenatis. Integer fringilla congue eros non fermentum. Sed dapibus pulvinar nibh 
            tempor porta. Cras ac leo purus. Mauris quis diam velit.
            </p>
            <ul id="navlist">
            <li id="park"><a href="./ImagePage"></a></li>
            <li id="building"><a href="./ImagePage"></a></li>
            <li id="trees"><a href="./ImagePage"></a></li>
            </ul>
        </div>
    );
};

export default ImagePage;