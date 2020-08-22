%rebase('base.tpl')
%import model


 

<div class="row">
  <div class="column left" style="background-color:#d2a679;">
    <h2>Navodila:</h2>
    <ol>
      <li>Najprej izberite težavnost.</li>
      <ul>
        <li>LAHKO predstavlja spomin velikosti 4*4, pri katerem iščeš pare.</li>
        <li>SREDNJE predstavlja spomin velikosti 4*6, prikaterem iščeš pare.</li>
        <li>TEŽKO predstavlja spomin velikosti 4*6, pri katerem iščeš trojice.</li>
      </ul>  
      <li>Čimbolje si oglej in zapomni ploščo.</li>
      <li>Poišči vse pare oziroma trojice.</li>
    </ol> 
  </div> 
  <div class="column right" style="background-color:#ffffff; text-align: center;">
    <h1 style='text-align: center;
     text-transform: uppercase;
     color: #800000; font-size:60px;' ><b>SPOMIN</b></h1>
  
   <tr>
        <td><b>Izberi težavnost:</b></td>
    </tr>
    
    <tr>
        <td>
            <form action="/nova_igra/" method="POST">
                <input type="radio" name="tezavnost" value="1"> Lahko<br>
                <input type="radio" name="tezavnost" value="2"> Srednje<br>
                <input type="radio" name="tezavnost" value="3"> Tezko<br>  
                <p><input type="submit" value="prični igro"></p>
            </form>
        </td>
    </tr>
  </div>
</div>



    
 
