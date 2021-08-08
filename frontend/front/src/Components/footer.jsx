import React from "react";
import "./footer.css";
import DLogo from "./Discordlogo.png";
import ILogo from "./Instalogo.png";
import MLogo from "./maillogo.png";
const FooterPanel = () => {
  return (

<div id="footer">
  <div id="footerleft">
    <h4>About</h4>
  </div>

  <div id="footerright">
    <h4>Privacy</h4>
  </div>
  <div id = "footerpics">
  <img id="DiscordLogo" src={DLogo} width = "30" alt="" />
  <img id="InstaLogo" src={ILogo} width = "36" alt="" />
  <img id="MailLogo" src={MLogo} width = "60" alt="" />
  </div>
</div>
  );
};

export default FooterPanel;