import "./ImagePage.css";

const ImagePage = () => {
    return (
        <body>
        <div>
            <img class='imga' id="rcorners3" src="/images/image1.jpg" alt="Jade rabbit"></img>
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
            <h2 id="borderimg">Select this text!</h2>
            <p>This is a navigation bar using image sprites</p>
            <ul id="navlist">
            <li id="home"><a href=".">1</a></li>
            <li id="prev"><a href="ImagePage">2</a></li>
            <li id="next"><a href="ImagePage">3</a></li>
            </ul>
            <div class="polaroid-container">
            <div>
            <h2>Responsive Polaroid Images / Cards</h2>
            <div className="polaroid-container">
                <div className="polaroid">
                    <img src="/images/cubic.jpg" alt="Cubic" style={{ width: '100%' }} />
                    <div className="container">
                        <p>Cubic Houses</p>
                    </div>
                </div>
                <div className="polaroid">
                    <img src="/images/cubic.jpg" alt="Cubic" style={{ width: '100%' }} />
                    <div className="container">
                        <p>Cubic Houses</p>
                    </div>
                </div>
            </div>
        </div>
        </div>
        </div>
        </body>
    );
};

export default ImagePage;