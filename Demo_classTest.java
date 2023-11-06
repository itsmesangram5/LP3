import static org.junit.Assert.*;

import org.junit.Test;

public class Demo_classTest {

	Demo_class obj=new Demo_class();   
	@Test  
	public void testSum() {  
	    assertEquals(2,obj.add(10, 15));  
	         }  
	
	@Test  
	public void testSum2() {  
	    assertEquals(25,obj.add(10, 15));  
	         }  
}
